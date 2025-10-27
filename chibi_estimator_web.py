# Developed by Ghost

import streamlit as st
import math

# Rarity data
rarities = {
    "Common": {"chance": 0.8928, "chibis": [
        "Achatina","Allosaurus","Amargasaurus","Ammonite","Anglerfish","Ankylosaurus",
        "Baryonyx","Beelzebufo","Bulbdog","Carno","Daeodon","Dilophosaur","Direbear",
        "Doedicurus","Featherlight","Gallimimus","Glowtail","Iguanodon","Kaprosuchus",
        "Karkinos","Kentrosaurus","Lymantria","Maewing","Mammoth","Manta","Mantis",
        "Megalania","Megaloceros","Megalodon","Megatherium","Mesopithecus","Moschops",
        "Pachy","Paraceratherium","Parasaur","Party Rex","Pelagornis","Phiomia",
        "Pteranodon","Pulmonoscorpius","Raptor","Rex","Rollrat","Sarco","Shadowmane",
        "Shinehorn","Spino","Stego","Terror Bird","Thylacoleo","Trike","Tropeognathus",
        "Vulture"
    ]},
    "Uncommon": {"chance": 0.0992, "chibis": [
        "Andrewsarchus","Animated Series Raptor","Araneo","Archaeopteryx","Argentavis",
        "Astrodelphis","Basilisk","Brontosaurus","Carbonemys","Castroides","Cnidaria",
        "Deinonychus","Diplodocus","Dodo","Dunkleosteus","Equus","Gasbag","Ghost Mantis",
        "Ghost Rex","Giganotosaurus","Gigantopithecus","Kairuku","Microraptor","Mosasaurus",
        "Otter","Oviraptor","Ovis","Procoptodon","Purlovia","Quetzal","Reaper","Reindeer",
        "Rhino","Rock Golem","Tapejara","Therizino","Thorny Dragon","Troodon","Yutyrannus",
        "Teeny Tiny Titano"
    ]},
    "Rare": {"chance": 0.005, "chibis": [
        "Bunny","Carcharodontosaurus","Desmodus","Direwolf","Easter Chick","Enforcer",
        "Fenrir","Fjordhawk","Festive Bulbdog","Festive Featherlight","Festive Glowtail",
        "Festive Shinehorn","Gacha Claus","Ghost Basilisk","Griffin","Managarmr","Onyc",
        "Plesiosaur","Queen Bee","Sabertooth","Seeker","Skeletal Brontosaurus","Skeletal Jerboa",
        "Skeletal Quetzal","Skeletal Stego","Skeletal Trike","Snow Owl","Straw Hat Otter",
        "TEK Raptor","Tek Stryder","Tusoteuthis","Velonasaur","Wyvern","X-Sabertooth",
        "Pair-o-Saurs","Sinomacrops"
    ]},
    "Very Rare": {"chance": 0.002, "chibis": [
        "Astrocetus","Bloodstalker","Bonnet Otter","Crystal Wyvern","Deal With It Dodo",
        "Dinopithecus","Ferox (Small)","Ghost Direwolf","Gigantopithecus Chieftan","Jerbunny",
        "Lovebird","Phoenix","Rock Drake","Skeletal Carno","Skeletal Giganotosaurus",
        "Skeletal Raptor","Skeletal Rex","Spooky Bulbdog","Spring Shinehorn","Stuffed Glowtail",
        "White-Collar Kairuku"
    ]},
    "Legendary": {"chance": 0.001, "chibis": [
        "Broodmother","Ferox (Large)","Magmasaur","Noglin","Skeletal Wyvern","The Witching Owl",
        "Unicorn","Voidwyrm","Zombie Wyvern","Festive Noglin"
    ]}
}

# Create combined drop-down list
dropdown_options = ["Every Chibi"]  # top
dropdown_options.extend(["Common","Uncommon","Rare","Very Rare","Legendary"])  # rarities
for rarity in rarities:
    dropdown_options.extend(rarities[rarity]["chibis"])

# Streamlit interface
st.set_page_config(page_title="Chibi Chance Estimator", page_icon="🐾")
st.title("Chibi Chance Estimator")
st.subheader("Developed by Ghost")

selection = st.selectbox("Select a Chibi or rarity:", [""] + dropdown_options)  # empty default

def harmonic_sum(n):
    return sum(1.0/i for i in range(1,n+1))

def expected_draws_single(chibi_name):
    for rarity, data in rarities.items():
        if chibi_name in data["chibis"]:
            p_rarity = data["chance"]
            n_in_rarity = len(data["chibis"])
            p_chibi = p_rarity / n_in_rarity
            expected = math.ceil(1 / p_chibi)
            chance_percent = p_chibi * 100
            return rarity, chance_percent, expected
    return None,None,None

def expected_draws_every_rarity(rarity):
    data = rarities[rarity]
    n = len(data["chibis"])
    p = data["chance"]
    H = harmonic_sum(n)
    expected = math.ceil((n * H) / p)
    return expected

def expected_draws_every_chibi():
    total = 0
    for rarity, data in rarities.items():
        n = len(data["chibis"])
        p = data["chance"]
        H = harmonic_sum(n)
        total += (n * H) / p
    return math.ceil(total)

# Calculate results
if selection == "":
    st.write("Please select a chibi from the drop-down menu. You may also type to search for your desired chibi.")
elif selection == "Every Chibi":
    expected = expected_draws_every_chibi()
    st.write(f"🎯 Target: Every Chibi")
    st.write(f"🧮 Expected number of draws to get all Chibis: {expected:,}")
elif selection in rarities:
    expected = expected_draws_every_rarity(selection)
    st.write(f"🎯 Target: Every {selection}")
    st.write(f"🧮 Expected number of draws to get all {selection} Chibis: {expected:,}")
else:
    rarity, chance_percent, expected = expected_draws_single(selection)
    st.write(f"🎯 Target: {selection}")
    st.write(f"🏷️ Rarity: {rarity}")
    st.write(f"🎲 Chance per draw: {chance_percent:.5f}%")
    st.write(f"🧮 Expected number of draws to get one: {expected:,}")
