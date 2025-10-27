# Developed by Ghost

import streamlit as st

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

# Build dropdown options
every_rarity_options = [f"Every {r}" for r in chibis.keys()]
all_chibis = [name for names in chibis.values() for name in names]

# Dropdowns
st.write("### Select a Chibi or rarity group")
chibi_choice = st.selectbox("Pick a Chibi:", ["--Select--"] + all_chibis)
rarity_choice = st.selectbox("Pick 'Every Rarity' option:", ["--Select--"] + every_rarity_options)

# Functions
def expected_draws_single_chibi(rarity, num_chibis):
    p_rarity = rarity_chances[rarity] / 100
    return num_chibis / p_rarity

def expected_draws_to_get_all(num_chibis, rarity):
    p_rarity = rarity_chances[rarity] / 100
    coupon_sum = sum(1 / (i+1) for i in range(num_chibis))
    return num_chibis * coupon_sum / p_rarity

def likelihood_in_n_draws(chance_per_draw_percent, draws):
    p = chance_per_draw_percent / 100
    return (1 - (1 - p) ** draws) * 100

# Display results
if chibi_choice != "--Select--":
    # Find the rarity
    rarity = None
    for r, names in chibis.items():
        if chibi_choice in names:
            rarity = r
            break
    if rarity:
        n = len(chibis[rarity])
        chance = (1 / n) * rarity_chances[rarity]
        draws = expected_draws_single_chibi(rarity, n)
        likelihood = likelihood_in_n_draws(chance, 1000)
        
        st.write(f"🎯 **Target:** {chibi_choice}")
        st.write(f"🏷️ **Rarity:** {rarity}")
        st.write(f"🎲 **Chance per draw:** {chance:.5f}%")
        st.write(f"🧮 **Expected number of draws to get one:** {draws:.2f}")
        st.write(f"💡 **Likelihood of obtaining within 1000 draws:** {likelihood:.2f}%")

if rarity_choice != "--Select--":
    rarity = rarity_choice.split()[1]
    n = len(chibis[rarity])
    draws = expected_draws_to_get_all(n, rarity)
    st.write(f"🧮 **Estimated number of draws to get {rarity_choice}:** {draws:.2f}")
