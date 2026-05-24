# Setup Guide — Garden Instagram Bot

## Step 1 — Create the Instagram account

1. Open the Instagram app on your phone
2. Create a new account — choose a name that fits the aesthetic, for example:
   - `@stoneandivy` / `@ivyandstone.garden`
   - `@the.reclaimed.garden`
   - `@nature.takes.back`
   - `@moss.and.manor`
3. **Switch to a Creator account** (required for API access):
   Settings → Account → Switch to Professional Account → Creator → Other

---

## Step 2 — Create a Facebook Page (required by Meta)

The Instagram Graph API requires a linked Facebook Page.

1. Go to https://www.facebook.com/pages/create
2. Create a Page with the same name as your Instagram account
3. Go to Instagram → Settings → Account → Linked Accounts → Facebook
4. Link your new Facebook Page to your Instagram account

---

## Step 3 — Create a Meta Developer App

1. Go to https://developers.facebook.com
2. Click **My Apps** → **Create App**
3. Choose **Other** → **Business**
4. Fill in the app name (e.g. "Garden Bot")
5. In the dashboard, find **Instagram Graph API** and click **Set Up**

---

## Step 4 — Get a long-lived access token

### 4a. Generate a short-lived token

1. Go to https://developers.facebook.com/tools/explorer
2. In **User or Page**, select your Facebook Page
3. Click **Generate Access Token**
4. Add these permissions:
   - `instagram_basic`
   - `instagram_content_publish`
   - `pages_read_engagement`
   - `pages_show_list`
5. Click **Generate Access Token** and copy the token

### 4b. Exchange for a long-lived token (60-day expiry)

Run this in your terminal (replace placeholders):

```bash
curl -i -X GET \
  "https://graph.facebook.com/v19.0/oauth/access_token
   ?grant_type=fb_exchange_token
   &client_id=YOUR_APP_ID
   &client_secret=YOUR_APP_SECRET
   &fb_exchange_token=SHORT_LIVED_TOKEN"
```

Copy the `access_token` value from the response.

### 4c. Get your Instagram User ID

```bash
curl "https://graph.facebook.com/v19.0/me/accounts?access_token=YOUR_LONG_LIVED_TOKEN"
```

Then use the page ID to find your Instagram user ID:

```bash
curl "https://graph.facebook.com/v19.0/YOUR_PAGE_ID?fields=instagram_business_account&access_token=YOUR_LONG_LIVED_TOKEN"
```

The `id` inside `instagram_business_account` is your `INSTAGRAM_USER_ID`.

---

## Step 5 — Set up imgbb (free image hosting)

1. Create a free account at https://imgbb.com
2. Go to https://api.imgbb.com and generate an API key
3. Copy the key

---

## Step 6 — Configure your environment

```bash
cp .env.example .env
# Edit .env and fill in all values
nano .env
```

---

## Step 7 — Install dependencies and run

```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Test a preview (no API calls, no posting)
python main.py preview

# Post one image right now
python main.py post

# Start the daily scheduler (runs at POST_TIME every day)
python main.py schedule
```

---

## Step 8 — Keep it running 24/7

### Option A — Run on your own machine with a simple service

On Linux/macOS, create a systemd service or use `screen`/`tmux`:

```bash
screen -S garden-bot
source venv/bin/activate
python main.py schedule
# Detach with Ctrl+A, D
```

### Option B — Deploy to a cloud server (recommended)

Any small VPS will do (e.g. Hetzner CX11, €4/month):

```bash
# On the server
git clone <your-repo>
cd garden-photo-bot
cp .env.example .env && nano .env
pip install -r requirements.txt

# Create systemd service
sudo nano /etc/systemd/system/garden-bot.service
```

```ini
[Unit]
Description=Garden Instagram Bot
After=network.target

[Service]
WorkingDirectory=/path/to/garden-photo-bot
ExecStart=/path/to/venv/bin/python main.py schedule
Restart=always
EnvironmentFile=/path/to/garden-photo-bot/.env

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable garden-bot
sudo systemctl start garden-bot
sudo systemctl status garden-bot
```

### Option C — GitHub Actions (free, zero infrastructure)

Add `.github/workflows/daily_post.yml` — the bot runs in GitHub's cloud once a day.
(Run `python main.py post` as a cron job step — no need for a persistent server.)

---

## Token refresh (every 60 days)

Long-lived tokens expire after 60 days. Refresh before expiry:

```bash
curl "https://graph.facebook.com/v19.0/oauth/access_token
  ?grant_type=fb_exchange_token
  &client_id=YOUR_APP_ID
  &client_secret=YOUR_APP_SECRET
  &fb_exchange_token=CURRENT_TOKEN"
```

---

## Instagram Growth Strategy

### Account setup (do once)
- Profile photo: one of your best generated images
- Bio: 2 lines max — describe the vibe, not the tool
  - Example: *"Where nature takes back what belongs to her. AI-imagined English gardens."*
- Link in bio: a linktree or simple landing page

### Content strategy
- Post every day at 09:00 local time (highest engagement window)
- Reply to every comment in the first hour (critical for algorithm)
- Post 1-2 Stories per day reposting your latest image
- Every 7th post: a "weekly favourite" carousel of the best 5 images

### Engagement loops
- Ask a question in every caption (see the captions module — already done)
- Use the "save" prompt ("save this for your mood board") — saves boost reach more than likes
- Follow accounts in adjacent niches: #cottagecore, #darkacademia, #historichouses

### Hashtag strategy (already implemented)
- 25 hashtags per post
- Mix: 10 niche + 4 aesthetic + 8 medium + 3 broad
- Rotate hashtags automatically (already handled by captions.py)
