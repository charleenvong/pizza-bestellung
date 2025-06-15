import mesop as me

@me.page(path="/pizza")
def main():
    me.text("Pizza-Bestellung")
    me.input(label="Name:")
    me.radio(label="Größe:", options=["Klein", "Mittel", "Groß"])
    me.checkbox(label="Extras:", options=["Käse", "Salami", "Pilze"])
    if me.button("Bestellen"):
        me.text("Danke! ")