"""
Prompt builder for the "Nature Reclaims Civilization" aesthetic.

Style DNA:
- Overgrown English manor/cottage gardens
- Stone architecture invaded by lush greenery
- Climbing plants conquering walls, archways, gates, urns
- Sophisticated stone decorative elements, partially swallowed by foliage
- Hyperrealistic DSLR photography, professional composition
"""

import random

# ── Focal architectural elements ──────────────────────────────────────────────
FOCAL_ELEMENTS = [
    "a moss-covered stone archway smothered in wisteria and ivy",
    "an ancient stone wall entirely consumed by cascading ivy and ferns",
    "a weathered iron gate half-hidden behind climbing roses and clematis",
    "a crumbling stone staircase draped in trailing ivy and wildflowers",
    "a centuries-old stone fountain encrusted with moss and surrounded by ferns",
    "a narrow garden path bordered by stone walls reclaimed by climbing hydrangea",
    "an old manor window framed by a thick curtain of wisteria in full bloom",
    "a stone garden bench enveloped in sprawling moss and creeping thyme",
    "a stone doorway wrapped in dark ivy, tendrils reaching across the lintel",
    "an overgrown pergola of stone and wrought iron draped in clematis and roses",
    "a collapsed stone wall with wildflowers and ivy erupting from every crack",
    "a Gothic stone window recess where ferns grow freely from the sill",
    "a stone-pillared gateway cloaked in Virginia creeper turning deep crimson",
    "a forgotten corner where stone meets earth, ivy cascading in thick curtains",
    "a walled garden entrance where climbing roses have sealed the gate with blooms",
]

# ── Foreground decorative elements (sophisticated, discreet) ──────────────────
DECORATIVE_ELEMENTS = [
    "an elegant stone urn half-buried in foliage",
    "a carved stone lion barely visible through dense ivy",
    "a weathered stone sundial wrapped in moss and clover",
    "a classical stone planter overflowing with ferns and trailing plants",
    "a stone sphere resting in a nest of moss",
    "a carved stone balustrade softened by creeping sedum",
    "an antique terracotta pot colonized by self-seeded wildflowers",
    "a stone trough overflowing with saxifrage and moss",
    "a barely visible stone finial emerging from a sea of greenery",
    "a stone birdbath draped in delicate ivy tendrils",
    "an old stone lantern pedestal swallowed by ferns",
    "a fragment of stone cornice lying in deep moss",
]

# ── Climbing and cascading plants ─────────────────────────────────────────────
CLIMBING_PLANTS = [
    "Hedera helix ivy",
    "Rosa 'Albertine' climbing roses",
    "Wisteria sinensis",
    "Clematis montana",
    "Virginia creeper (Parthenocissus quinquefolia)",
    "Hydrangea petiolaris",
    "Lonicera honeysuckle",
    "Trachelospermum jasminoides star jasmine",
    "Parthenocissus tricuspidata Boston ivy",
    "Akebia quinata",
]

GROUND_PLANTS = [
    "dense ferns and hart's tongue fern",
    "creeping moss and liverwort",
    "Alchemilla mollis lady's mantle",
    "wild violets and wood anemones",
    "self-seeded foxgloves",
    "Epimedium and Solomon's seal",
    "Geranium phaeum mourning widow",
    "Helleborus orientalis lenten rose",
]

# ── Lighting conditions ───────────────────────────────────────────────────────
LIGHTING = [
    "bathed in warm golden hour light, long shadows stretching across stone",
    "in soft diffused morning mist, dew catching the early light",
    "under gentle dappled sunlight filtering through a forest canopy",
    "in the luminous glow of a cloudy overcast day, colours richly saturated",
    "caught in a shaft of late-afternoon sun piercing through heavy foliage",
    "after a rainfall, every stone surface glistening with moisture",
    "in the blue-green light of a foggy morning",
    "in warm autumn slanted light, leaves glowing amber and gold",
    "in the cool luminosity of an overcast spring morning",
    "in dreamy soft-focus backlight, haze diffusing the background",
]

# ── Seasons ───────────────────────────────────────────────────────────────────
SEASONS = [
    "in high summer, foliage at peak lushness",
    "in late spring, wisteria and roses beginning to bloom",
    "in early autumn, ivy turning rust and crimson",
    "in deep winter, frost on moss and bare climbing stems tracing the stone",
    "in mid-spring, fresh new leaf growth bright against old stone",
    "in the height of rose season, blooms spilling everywhere",
    "in late autumn, fallen leaves carpeting the ground",
    "in early spring, the first ferns unfurling from stone crevices",
]

# ── Camera / photography style ────────────────────────────────────────────────
CAMERA_STYLES = [
    "shot with a Canon EOS R5, 85mm f/1.4 lens, ultra-shallow depth of field, bokeh background",
    "photographed with a Nikon Z7, 50mm f/1.2, fine botanical detail in sharp focus",
    "taken with a medium-format Hasselblad X2D, extraordinary tonal richness and depth",
    "shot with a Sony A7R V, 35mm f/1.8, wide perspective capturing the full architecture",
    "photographed with a vintage Leica M lens, subtle halation and film-like rendering",
    "Canon 5D Mark IV, 100mm macro lens, mosses and lichens in extraordinary detail",
]

# ── Mood / atmosphere ─────────────────────────────────────────────────────────
MOODS = [
    "romantic and melancholic, time suspended",
    "mysterious and ancient, whispering of forgotten stories",
    "serene and otherworldly, as if from a dream",
    "lush and overwhelming, nature triumphant",
    "quiet and contemplative, the silence palpable",
    "ethereal and painterly, reality softened by beauty",
    "wild and untamed, civilization politely retreating",
]

BASE_QUALITY = (
    "hyperrealistic professional garden photography, photorealistic render, "
    "8K resolution, award-winning composition, National Geographic quality, "
    "no people, no text, no watermarks"
)

NEGATIVE_HINTS = (
    "avoid overly manicured or tidy appearance, avoid cartoon or illustration style, "
    "avoid symmetrical or formal garden layout"
)


def build_prompt() -> str:
    focal = random.choice(FOCAL_ELEMENTS)
    decor = random.choice(DECORATIVE_ELEMENTS)
    climber = random.choice(CLIMBING_PLANTS)
    ground = random.choice(GROUND_PLANTS)
    light = random.choice(LIGHTING)
    season = random.choice(SEASONS)
    camera = random.choice(CAMERA_STYLES)
    mood = random.choice(MOODS)

    prompt = (
        f"{focal}, with {decor} in the foreground, "
        f"dense {climber} consuming the stone surfaces, "
        f"{ground} carpeting every shadow. "
        f"The scene is {season}. "
        f"Lighting: {light}. "
        f"Atmosphere: {mood}. "
        f"{camera}. "
        f"{BASE_QUALITY}. "
        f"{NEGATIVE_HINTS}."
    )

    return prompt


def build_variation_prompt(theme: str) -> str:
    """Generate a prompt for a specific weekly theme."""
    themes = {
        "doorways": [
            "A stone doorway or gate completely framed by climbing plants",
            "An arched entrance in an English manor garden wall, ivy-clad",
        ],
        "walls": [
            "A long stone wall entirely colonized by ivy and ferns",
            "A crumbling garden wall where nature has taken full possession",
        ],
        "water": [
            "A moss-encrusted stone fountain where water still trickles",
            "A small stone pond surrounded by lush ferns and overhanging ivy",
        ],
        "statuary": [
            "A classical stone statue almost entirely hidden by climbing ivy",
            "A stone urn overflowing with plants in an overgrown garden",
        ],
        "paths": [
            "A narrow stone path disappearing into dense overgrown garden",
            "Ancient stone steps covered in moss leading into a secret garden",
        ],
    }

    options = themes.get(theme, [build_prompt()])
    base = random.choice(options)
    light = random.choice(LIGHTING)
    season = random.choice(SEASONS)
    camera = random.choice(CAMERA_STYLES)

    return (
        f"{base}. "
        f"{season}. "
        f"Lighting: {light}. "
        f"{camera}. "
        f"{BASE_QUALITY}."
    )
