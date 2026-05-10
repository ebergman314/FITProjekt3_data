def q9_visualization(data, title):

# se över*****************************************************************
    years = [
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        2023,
    ]  # sorted(data.keys())
    # ny********************
    years = sorted({k[1] for k in data.keys()})

    values_birkaland = [data[("Birkaland", y)] for y in years]
#**************se över "values_egentliga_finland" var skrivna 2 gånger*******************************************************************************
    values_egentliga_finland = [data[("Egentliga Finland", y)] for y in years]
    values_egentliga_tavastland = [data[("Egentliga Tavastland", y)] for y in years]
    values_kajanaland = [data[("Kajanaland", y)] for y in years]
    values_kymmenedalen = [data[("Kymmenedalen", y)] for y in years]
    values_lappland = [data[("Lappland", y)] for y in years]
    values_mellersta_finland = [data[("Mellersta Finland", y)] for y in years]
    values_mellersta_österbotten = [data[("Mellersta Österbotten", y)] for y in years]
    values_norra_karelen = [data[("Norra Karelen", y)] for y in years]
    values_norra_savolax = [data[("Norra Savolax", y)] for y in years]
    values_norra_österbotten = [data[("Norra Österbotten", y)] for y in years]
    values_nyland = [data[("Nyland", y)] for y in years]
    values_päijänne_tavastland = [data[("Päijänne-Tavastland", y)] for y in years]
    values_satakunta = [data[("Satakunta", y)] for y in years]
    values_södra_karelen = [data[("Södra Karelen", y)] for y in years]
    values_södra_savolax = [data[("Södra Savolax", y)] for y in years]
    values_södra_österbotten = [data[("Södra Österbotten", y)] for y in years]
    values_åland = [data[("Åland", y)] for y in years]
    values_österbotten = [data[("Österbotten", y)] for y in years]

    fig, ax = plt.subplots(figsize=(10, 5))
    (line1,) = ax.plot(years, values_birkaland, marker="o", label="Birkaland")
    (line2,) = ax.plot(
        years, values_egentliga_finland, marker="o", label="Egentliga Finland"
    )
    (line3,) = ax.plot( #ändring från "values_egentliga_finland" till "values_egentliga_tavastland"***************************************
        years, values_egentliga_tavastland, marker="o", label="Egentliga Tavastland"
    )
    (line4,) = ax.plot(years, values_kajanaland, marker="o", label="Kajanaland")
    (line5,) = ax.plot(years, values_kymmenedalen, marker="o", label="Kymmendalen")
    (line6,) = ax.plot(years, values_lappland, marker="o", label="Lappland")
    (line7,) = ax.plot(
        years, values_mellersta_finland, marker="o", label="Mellersta Finland"
    )
    (line8,) = ax.plot(
        years, values_mellersta_österbotten, marker="o", label="Mellersta Österbotten"
    )
    (line9,) = ax.plot(years, values_norra_karelen, marker="o", label="Norra Karelen")
    (line10,) = ax.plot(years, values_norra_savolax, marker="o", label="Norra Savolax")
    (line11,) = ax.plot(
        years, values_norra_österbotten, marker="o", label="Norra Österbotten"
    )
    (line12,) = ax.plot(years, values_nyland, marker="o", label="Nyland")
    (line13,) = ax.plot(
        years, values_päijänne_tavastland, marker="o", label="Päijänne-Tavastland"
    )
    (line14,) = ax.plot(years, values_satakunta, marker="o", label="Satakunta")
    (line15,) = ax.plot(years, values_södra_karelen, marker="o", label="Södra Karelen")
    (line16,) = ax.plot(years, values_södra_savolax, marker="o", label="Södra Savolax")
    (line17,) = ax.plot(
        years, values_södra_österbotten, marker="o", label="Södra Österbotten"
    )
    (line18,) = ax.plot(years, values_åland, marker="o", label="Åland")
    (line19,) = ax.plot(years, values_österbotten, marker="o", label="Österbotten")

    ax.set_xlabel("År")
    ax.set_ylabel("Antal hushåll/personer")
    ax.set_title(title)
    ax.grid(True)
    ax.legend(
        handles=[
            line1,
            line2,
            line3,
            line4,
            line5,
            line6,
            line7,
            line8,
            line9,
            line10,
            line11,
            line12,
            line13,
            line14,
            line15,
            line16,
            line17,
            line18,
            line19,
        ]
    )
    plt.xticks(years, rotation=45)
    plt.tight_layout()
    center(fig)     # Centrera fönstret på skärmen
    plt.show()
