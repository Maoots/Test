"""
Caption and hashtag generator for the garden Instagram account.

Strategy for maximum reach:
- Poetic short caption (creates emotion, encourages saves & shares)
- A question or CTA to trigger comments (boosts algorithmic reach)
- 3-tier hashtag mix: niche (most effective), medium, broad
"""

import random

# ── Poetic captions ───────────────────────────────────────────────────────────
CAPTIONS = [
    "She didn't fight the garden. She let it win.\n\n{cta}",
    "The ivy remembers everything the stone has forgotten.\n\n{cta}",
    "Nature is patient. Stone is not.\n\n{cta}",
    "Between the cracks, everything blooms.\n\n{cta}",
    "Time moves differently here — measured in seasons, not hours.\n\n{cta}",
    "The garden doesn't ask permission.\n\n{cta}",
    "What the architect built, the ivy completed.\n\n{cta}",
    "A wall is just a trellis waiting to be discovered.\n\n{cta}",
    "Here, the wilderness and the cultivated have made their peace.\n\n{cta}",
    "Every stone has a fern waiting inside it.\n\n{cta}",
    "The gate is still there. Somewhere beneath the roses.\n\n{cta}",
    "Moss is the stone's way of growing old gracefully.\n\n{cta}",
    "The garden took back what was always hers.\n\n{cta}",
    "Civilisation paused here, and nature filled the silence.\n\n{cta}",
    "Somewhere between ruin and renewal, this garden found its voice.\n\n{cta}",
    "Some gardens are designed. This one simply happened.\n\n{cta}",
    "The wall stood for centuries. The ivy arrived and made it permanent.\n\n{cta}",
    "These roots go deeper than the stone.\n\n{cta}",
    "She wound herself around every hard edge and softened them all.\n\n{cta}",
    "Not abandoned — returned.\n\n{cta}",
    "Under every formal garden, a wild one waits.\n\n{cta}",
    "The sundial still counts. The garden stopped caring long ago.\n\n{cta}",
    "Nothing more patient than a seed in a stone wall.\n\n{cta}",
    "The architecture was a suggestion. The ivy took notes.\n\n{cta}",
    "Ruins are just gardens in waiting.\n\n{cta}",
]

# ── Calls to action ───────────────────────────────────────────────────────────
CTAS = [
    "Does a place like this exist near you? 🌿",
    "Which plant would you plant first against that stone wall?",
    "Save this for a day when you need to slow down.",
    "Tag someone who would love to sit here for a while.",
    "What does this place make you feel? Tell me below.",
    "Would you restore it — or leave it exactly as it is?",
    "Name one plant you see in this image 🌱",
    "Save for your next garden project or mood board.",
    "What season do you picture yourself here?",
    "Drop a 🌿 if this is your kind of garden.",
]

# ── Hashtag pools ─────────────────────────────────────────────────────────────
# Niche tags (lowest competition, highest engagement rate)
NICHE_TAGS = [
    "#overgrowngarden",
    "#englishcottagegarden",
    "#stonewall garden",
    "#naturereclaimscity",
    "#mossgarden",
    "#climingplants",
    "#ivywall",
    "#gardenruins",
    "#wildgarden",
    "#botanicalgarden",
    "#gardenarchitecture",
    "#heritagegardens",
    "#wisterialovers",
    "#climbingroses",
    "#romantickgarden",
    "#cottagegardening",
    "#naturallandscape",
    "#secretgarden",
    "#enchantedgarden",
    "#hiddengardens",
    "#gardenphotography",
    "#stonegarden",
    "#mossandstone",
    "#overgrown",
    "#vinecovered",
]

# Medium reach tags
MEDIUM_TAGS = [
    "#gardendesign",
    "#gardenlife",
    "#gardenlovers",
    "#gardeninglife",
    "#plantlover",
    "#greenspace",
    "#botanica",
    "#horticuture",
    "#plantsofinstagram",
    "#gardeninspiration",
    "#outdoorliving",
    "#natureinspired",
    "#landscapedesign",
    "#outdoorspaces",
    "#gardengoals",
    "#livingwalls",
    "#wildflowers",
    "#ferns",
    "#plantlife",
    "#englishgarden",
]

# Broad reach tags (use sparingly — 3-5 max)
BROAD_TAGS = [
    "#nature",
    "#garden",
    "#plants",
    "#green",
    "#photography",
    "#naturephotography",
    "#landscape",
    "#outdoor",
]

# Aesthetic/lifestyle tags for discovery
AESTHETIC_TAGS = [
    "#cottagecore",
    "#darkacademia",
    "#goblincore",
    "#fairytaleaesthetic",
    "#mossaesthetic",
    "#romanticaesthetic",
    "#witchyaesthetic",
    "#moodyaesthetic",
    "#darkromantic",
    "#forestcore",
    "#naturecore",
    "#antiquegarden",
    "#victoriangarden",
]


def build_caption() -> str:
    caption_template = random.choice(CAPTIONS)
    cta = random.choice(CTAS)
    caption = caption_template.format(cta=cta)

    hashtags = _build_hashtags()

    return f"{caption}\n.\n.\n.\n{hashtags}"


def _build_hashtags() -> str:
    selected = (
        random.sample(NICHE_TAGS, k=min(10, len(NICHE_TAGS)))
        + random.sample(AESTHETIC_TAGS, k=4)
        + random.sample(MEDIUM_TAGS, k=8)
        + random.sample(BROAD_TAGS, k=3)
    )
    random.shuffle(selected)
    return " ".join(selected)
