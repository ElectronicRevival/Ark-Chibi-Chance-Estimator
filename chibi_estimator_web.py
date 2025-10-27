# Developed by Ghost

import streamlit as st
import math

# Window title
st.set_page_config(page_title="Chibi Drop Estimator - Developed by Ghost")

# Rarity chances (in %)
rarity_chances = {
    "Common": 89.28,
    "Uncommon": 9.92,
    "Rare": 0.5,
    "Very Rare": 0.2,
    "Legendary": 0.1
}

# Chibis per rarity (cleaned names)
chibis = {
    "Common": [
        "Achatina","Allosaurus","Amargasaurus","Ammonite","Anglerfish","Ankylosaurus","Baryonyx",
        "Beelzebufo","Bulbdog","Carno","Daeodon","Dilophosaur","Direbear","Doedicurus","Featherlight",
        "Gallimimus","Glowtail","Iguanodon","Kaprosuchus","Karkinos","Kentrosaurus","Lymantria",
        "Maewing","Mammoth","Manta","Mantis","Megalania","Megaloceros","Megalodon","Megatherium",
        "Mesopithecus","Moschops","Pachy","Paraceratherium","Parasaur","Party Rex","Pelagornis",
        "Phiomia","Pteranodon","Pulmonoscorpius","Raptor","Rex","Rollrat","Sarco","Shadowmane",
        "Shinehorn","Spino","Stego","Terror Bird","Thylacoleo","Trike","Tropeognathus","Vulture"
    ],
    "Uncommon": [
        "Andrewsarchus","Animated Series Raptor","Araneo","Archaeopteryx","Argentavis","Astrodelphis",
        "Basilisk","Brontosaurus","Carbonemys","Castroides","Cnidaria","Deinonychus","Diplodocus","Dodo",
        "Dunkleosteus","Equus","Gasbag","Ghost Mantis","Ghost Rex","Giganotosaurus","Gigantopithecus",
        "Kairuku","Microraptor","Mosasaurus","Otter","Oviraptor","Ovis","Procoptodon","Purlovia","Quetzal",
        "Reaper","Reindeer","Rhino","Rock Golem","Tapejara","Therizino","Thorny Dragon","Troodon",
        "Yutyrannus","Teeny Tiny Titano"
    ],
    "Rare": [
        "Bunny","Carcharodontosaurus","Desmodus","Direwolf","Easter Chick","Enforcer","Fenrir","Fjordhawk",
        "Festive Bulbdog","Festive Featherlight","Festive Glowtail","Festive Shinehorn","Gacha Claus",
        "Ghost Basilisk","Griffin","Managarmr","Onyc","Plesiosaur","Queen Bee","Sabertooth","Seeker",
        "Skeletal Brontosaurus","Skeletal Jerboa","Skeletal Quetzal","Skeletal Stego","Skeletal Trike",
        "Snow Owl","Straw Hat Otter","TEK Raptor","Tek Stryder","Tusoteuthis","Velonasaur","Wyvern",
        "X-Sabertooth","Pair-o-Saurs","Sinomacrops"
    ],
    "Very Rare": [
        "Astrocetus","Bloodstalker","Bonnet Otter","Crystal Wyvern","Deal With It Dodo","Dinopithecus",
        "Ferox (Small)","Ghost Direwolf","Gigantopithecus Chieftan","Jerbunny","Lovebird","Phoenix",
        "Rock Drake","Skeletal Carno","Skeletal Giganotosaurus","Skeletal Raptor","Skeletal Rex",
        "Spooky Bulbdog","Spring Shinehorn","Stuffed Glowtail","White-Collar Kairuku"
    ],
    "Legendary": [
        "Broodmother","Ferox (Large)","Magmasaur","Noglin","Skeletal Wyvern","The Witching Owl",
        "Unicorn","Voidwyrm","Zombie Wyvern","Festive Noglin"
    ]
}

# Build single dropdown options
dropdown_options = ["Every Chibi"]  # First option
# Add rarities
dropdown_options += [f"Every {r}" for r in chibis.keys()]
# Add individual chibis alphabetically
all_chibis = sorted([name for names in chibis.values() for name in names])
dropdown_options += all_chibis

# Dropdown
st.write("### Select a Chibi, 'Every Rarity' or 'Every Chibi'")
selection = st.selectbox("Pick an option:", dropdown_options)

# Functions
def expected_draws_single_chibi(rarity, num_chibis):
    p_rarity = rarity_chances[rarity] / 100
    draws = num_chibis / p_rarity
    return math.ceil(draws)  # round up

def expected_draws_to_get_all(num_chibis, rarity=None):
    if rarity:
        p_rarity = rarity_chances[rarity] / 100
    else:
        p_rarity = 1  # every chibi, overall probability treated as 1 per draw
    coupon_sum = sum(1 / (i+1) for i in range(num_chibis))
    draws = num_chibis * coupon_sum / p_rarity
    return math.ceil(draws)  # round up

# Display results
if selection == "Every Chibi":
    total_chibis = sum(len(names) for names in chibis.values())
    draws = expected_draws_to_get_all(total_chibis)
    st.write(f"🧮 **Estimated number of draws to get every Chibi:** {draws}")
elif selection.startswith("Every "):  # Rarity group
    rarity = selection.split()[1]
    n = len(chibis[rarity])
    draws = expected_draws_to_get_all(n, rarity)
    st.write(f"🧮 **Estimated number of draws to get {selection}:** {draws}")
else:  # Single chibi
    rarity = None
    for r, names in chibis.items():
        if selection in names:
            rarity = r
            break
    if rarity:
        n = len(chibis[rarity])
        chance = (1 / n) * rarity_chances[rarity]
        draws = expected_draws_single_chibi(rarity, n)
        st.write(f"🎯 **Target:** {selection}")
        st.write(f"🏷️ **Rarity:** {rarity}")
        st.write(f"🎲 **Chance per draw:** {chance:.5f}%")
        st.write(f"🧮 **Expected number of draws to get one:** {draws}")
