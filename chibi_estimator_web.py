# Developed by Ghost
import streamlit as st
import math

# Define Chibi lists and rarity chances
chibis = {
    "Common": [
        "Chibi-Achatina","Chibi-Allosaurus","Chibi-Amargasaurus","Chibi-Ammonite",
        "Chibi-Anglerfish","Chibi-Ankylosaurus","Chibi-Baryonyx","Chibi-Beelzebufo",
        "Chibi-Bulbdog","Chibi-Carno","Chibi-Daeodon","Chibi-Dilophosaur",
        "Chibi-Direbear","Chibi-Doedicurus","Chibi-Featherlight","Chibi-Gallimimus",
        "Chibi-Glowtail","Chibi-Iguanodon","Chibi-Kaprosuchus","Chibi-Karkinos",
        "Chibi-Kentrosaurus","Chibi-Lymantria","Chibi-Maewing","Chibi-Mammoth",
        "Chibi-Manta","Chibi-Mantis","Chibi-Megalania","Chibi-Megaloceros",
        "Chibi-Megalodon","Chibi-Megatherium","Chibi-Mesopithecus","Chibi-Moschops",
        "Chibi-Pachy","Chibi-Paraceratherium","Chibi-Parasaur","Chibi Party Rex",
        "Chibi-Pelagornis","Chibi-Phiomia","Chibi-Pteranodon","Chibi-Pulmonoscorpius",
        "Chibi-Raptor","Chibi-Rex","Chibi-Rollrat","Chibi-Sarco","Chibi-Shadowmane",
        "Chibi-Shinehorn","Chibi-Spino","Chibi-Stego","Chibi-Terror Bird",
        "Chibi-Thylacoleo","Chibi-Trike","Chibi-Tropeognathus","Chibi-Vulture"
    ],
    "Uncommon": [
        "Chibi-Andrewsarchus","Chibi-Animated Series Raptor","Chibi-Araneo",
        "Chibi-Archaeopteryx","Chibi-Argentavis","Chibi-Astrodelphis","Chibi-Basilisk",
        "Chibi-Brontosaurus","Chibi-Carbonemys","Chibi-Castroides","Chibi-Cnidaria",
        "Chibi-Deinonychus","Chibi-Diplodocus","Chibi-Dodo","Chibi-Dunkleosteus",
        "Chibi-Equus","Chibi-Gasbag","Chibi-Ghost Mantis","Chibi-Ghost Rex",
        "Chibi-Giganotosaurus","Chibi-Gigantopithecus","Chibi-Kairuku","Chibi-Microraptor",
        "Chibi-Mosasaurus","Chibi-Otter","Chibi-Oviraptor","Chibi-Ovis","Chibi-Procoptodon",
        "Chibi-Purlovia","Chibi-Quetzal","Chibi-Reaper","Chibi-Reindeer","Chibi-Rhino",
        "Chibi-Rock Golem","Chibi-Tapejara","Chibi-Therizino","Chibi-Thorny Dragon",
        "Chibi-Troodon","Chibi-Yutyrannus","Teeny Tiny Titano"
    ],
    "Rare": [
        "Chibi-Bunny","Chibi-Carcharodontosaurus","Chibi-Desmodus","Chibi-Direwolf",
        "Chibi-Easter Chick","Chibi-Enforcer","Chibi-Fenrir","Chibi-Fjordhawk",
        "Chibi-Festive Bulbdog","Chibi-Festive Featherlight","Chibi-Festive Glowtail",
        "Chibi-Festive Shinehorn","Chibi-Gacha Claus","Chibi-Ghost Basilisk","Chibi-Griffin",
        "Chibi-Managarmr","Chibi-Onyc","Chibi-Plesiosaur","Chibi-Queen Bee","Chibi-Sabertooth",
        "Chibi-Seeker","Chibi-Skeletal Brontosaurus","Chibi-Skeletal Jerboa","Chibi-Skeletal Quetzal",
        "Chibi-Skeletal Stego","Chibi-Skeletal Trike","Chibi-Snow Owl","Chibi-Straw Hat Otter",
        "Chibi-TEK Raptor","Chibi-Tek Stryder","Chibi-Tusoteuthis","Chibi-Velonasaur",
        "Chibi-Wyvern","Chibi-X-Sabertooth","Pair-o-Saurs Chibi","Chibi-Sinomacrops"
    ],
    "Very Rare": [
        "Chibi-Astrocetus","Chibi-Bloodstalker","Chibi-Bonnet Otter","Chibi-Crystal Wyvern",
        "Chibi-Deal With It Dodo","Chibi-Dinopithecus","Chibi-Ferox (Small)","Chibi-Ghost Direwolf",
        "Chibi-Gigantopithecus Chieftan","Chibi-Jerbunny","Chibi-Lovebird","Chibi-Phoenix",
        "Chibi-Rock Drake","Chibi-Skeletal Carno","Chibi-Skeletal Giganotosaurus","Chibi-Skeletal Raptor",
        "Chibi-Skeletal Rex","Chibi-Spooky Bulbdog","Chibi-Spring Shinehorn","Chibi-Stuffed Glowtail",
        "White-Collar Kairuku"
    ],
    "Legendary": [
        "Chibi-Broodmother","Chibi-Ferox (Large)","Chibi-Magmasaur","Chibi-Noglin",
        "Chibi-Skeletal Wyvern","Chibi-The Witching Owl","Chibi-Unicorn","Chibi-Voidwyrm",
        "Chibi-Zombie Wyvern","Chibi-Festive Noglin"
    ]
}

rarity_chances = {
    "Common": 0.8928,
    "Uncommon": 0.0992,
    "Rare": 0.005,
    "Very Rare": 0.002,
    "Legendary": 0.001
}

# Streamlit App
st.title("ARK Chibi Estimator - Developed by Ghost")

# Dropdown for selection
options = ["Every Chibi"]
for r in chibis.keys():
    options.append(f"Every {r}")
for r, names in chibis.items():
    options.extend(names)

selection = st.selectbox("Select a Chibi, rarity, or 'Every Chibi'", options)

def chance_single(chibi_name):
    # Find the rarity
    for r, names in chibis.items():
        if chibi_name in names:
            p_rarity = rarity_chances[r]
            n = len(names)
            chance = p_rarity / n
            return chance
    return None

def expected_draws_single(chibi_name):
    chance = chance_single(chibi_name)
    if chance:
        return 1 / chance
    return None

def expected_draws_every(rarity=None):
    if rarity:
        names = chibis[rarity]
        p_rarity = rarity_chances[rarity]
    else:
        # All Chibis
        names = [c for lst in chibis.values() for c in lst]
        p_rarity = 1.0
    draws = 0.0
    remaining = len(names)
    for k in range(len(names)):
        draws += 1 / (p_rarity * (remaining - k)/len(names))
    return draws

# Calculation
if selection.startswith("Every"):
    if selection == "Every Chibi":
        draws = expected_draws_every()
        st.write(f"Expected number of draws to obtain **every Chibi**: {draws:.0f}")
    else:
        rarity = selection.split()[1]
        draws = expected_draws_every(rarity)
        st.write(f"Expected number of draws to obtain **every {rarity} Chibi**: {draws:.0f}")
else:
    chance = chance_single(selection)
    draws = expected_draws_single(selection)
    st.write(f"Chance per draw for **{selection}**: {chance*100:.5f}%")
    st.write(f"Expected number of draws to obtain **{selection}**: {draws:.0f}")
