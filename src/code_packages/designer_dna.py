from __future__ import annotations
import pandas as pd

# Designer DNA dictionary (copied from your notebook)
designer_dna={
    "Ann Demulemeester" :  """Poetic avant-garde minimalism rooted in romantic darkness. Dominated 
    by black, off-white, and muted neutrals, with elongated, draped, and layered silhouettes. 
    Common materials include washed cotton, silk, wool, linen, leather, and shearling, often left 
    raw or softly distressed. Patterns are minimal or absent, occasionally subtle stripes or textural 
    contrasts rather than prints. Core categories include tailoring, fluid coats, blazers, shirts, 
    trousers, boots, and scarves. Appeals to an introspective, artistic audience drawn to emotional 
    expression, literary references, and understated rebellion rather than overt trends.""" ,

    "Rick Owens" : """Brutalist avant-garde with exaggerated proportions and architectural 
                silhouettes. Heavy use of leather, calfskin, lambskin, thick jersey, wool, denim, 
                and cashmere blends. Predominantly monochrome palettes—black, dust, bone, grey—with 
                minimal prints and focus on texture and structure. Signature categories include oversized
                outerwear, elongated tops, drop-crotch trousers, boots, platform footwear, and statement 
                leather jackets. Targets a subcultural, fashion-forward audience interested in radical 
                self-expression, dystopian aesthetics, and sculptural clothing.""" ,

    
    "Dirk Bikkembergs": """Performance-driven masculinity combining sportswear and tailoring. 
    Materials emphasize technical fabrics, leather, neoprene, cotton blends, and structured knits. 
    Patterns are minimal, often graphic stripes or logo elements inspired by football culture. 
    Categories focus on menswear staples: tailored suits, athletic outerwear, boots, sneakers, and 
    body-conscious silhouettes. Designed for a confident, physically expressive audience that values 
    strength, discipline, and movement.""" ,

    "Dries Van Noten" : """Intellectual maximalism blending refined tailoring with rich surface design. 
    Luxurious fabrics such as silk, brocade, jacquard, velvet, wool, and embroidered textiles are 
    central. Known for complex patterns, florals, abstract prints, and layered textures. Garment 
    categories include tailored jackets, coats, blouses, trousers, skirts, and eveningwear. Appeals 
    to culturally curious wearers who value craftsmanship, color mastery, and expressive elegance.""",

    "Carol Christian Poell" : """Radical experimental fashion focused on material research and 
    anatomical construction. Uses hand-treated leather, horse leather, rubberized cotton, 
    resin-coated fabrics, and garment-dyed textiles. Patterns are absent; emphasis is on texture, 
    seams, scars, and construction marks. Categories include leather jackets, boots, trousers, and 
    tightly engineered garments. Attracts a niche audience of avant-garde collectors who value 
    obsessive craftsmanship and conceptual depth over wearability.""",

    "Boris Bidjan Saberi" : """Dark utilitarian avant-garde with nomadic and industrial 
    undertones. Materials include treated cotton, linen, leather, technical blends, and 
    hand-dyed fabrics. Patterns are subtle or absent, relying on layered construction and 
    surface treatment. Categories focus on jackets, hooded outerwear, trousers, boots, and 
    functional layering pieces. Designed for an urban, experimental audience drawn to ritualistic 
    aesthetics and artisanal streetwear.""",

    "Isaac Sellam Experience": """Experimental luxury leatherwear emphasizing innovation and precision. 
    Primary materials are high-grade leather, bonded leather, metal hardware, and technical textiles.
    Patterns are minimal; detailing comes from cuts, panels, and closures. Core categories include leather 
    jackets, coats, vests, and modular garments. Appeals to a design-conscious audience seeking futuristic,
    engineered luxury with tactile depth.""",

    "Roberto Cavalli": """Glamorous maximalism centered on sensuality and visual impact.
    Materials include silk, velvet, leather, satin, and embellished textiles. 
    Signature patterns include animal prints, baroque motifs, and bold graphic designs. 
    Categories range from body-hugging dresses and eveningwear to statement outerwear and denim.
    Targets a confident, extroverted audience drawn to luxury, drama, and overt sexuality.""",

    "Yohji Yamamoto" : """Philosophical avant-garde defined by volume, asymmetry, and monochrome 
    palettes. Materials include wool gabardine, cotton, linen, and fluid synthetics. Prints are rare,
    with occasional abstract or calligraphic motifs. Categories focus on oversized coats, trousers, 
    shirts, and layered silhouettes. Appeals to intellectual wearers who appreciate conceptual design 
    and nonconformity.""",

    "Balenciaga": """Conceptual contemporary fashion blending irony and exaggeration. Materials span 
    denim, technical synthetics, leather, and jersey. Patterns often reference logos, graphics, or 
    distorted classics. Categories include oversized outerwear, streetwear, footwear, and reimagined
    basics. Designed for trend-aware, culturally engaged audiences who value provocation and modern 
    commentary.""", 

    "Vivienne Westwood": """Punk rebellion mixed with historical tailoring. Materials include tartan 
    wool, corsetry fabrics, tweed, and structured cottons. Patterns feature plaids, slogans, and 
    historical references. Categories include corsets, tailoring, dresses, and statement outerwear. 
    Appeals to politically aware, expressive individuals who embrace fashion as protest.""",

    "Marc le Bihan": """Subtle avant-garde with refined craftsmanship. 
    Uses wool, silk, cotton, and muted textured fabrics. Patterns are minimal or tonal. 
    Categories include delicate tailoring, dresses, and understated outerwear. Appeals to a 
    quiet, design-literate audience valuing restraint and nuance.""",

    "Yves Saint Laurent": """Timeless Parisian elegance with sensual edge. Materials include fine 
    wool, silk, leather, and velvet. Patterns are classic or minimal. Categories include tuxedos, 
    tailoring, eveningwear, and leather jackets. Appeals to confident wearers seeking sophistication 
    with attitude.""",

    "Schiaparelli": """Surrealist couture emphasizing sculptural artistry. 
    Uses embellished fabrics, metallics, embroidery, and couture techniques. 
    Patterns are symbolic and artistic. Categories include couture gowns and 
    statement pieces. Appeals to collectors and art-driven audiences.""",

    "Dior by John Galliano": """Theatrical couture blending history and fantasy. 
    Luxurious silks, embroidery, corsetry, and layered textiles dominate. 
    Patterns are ornate and narrative-driven. Categories include gowns, tailored suits, 
    and couture pieces. Appeals to romantic, expressive luxury consumers.""",

    "Dior by Hedi Slimane": """Lean, rock-inspired tailoring. Materials include fine wool, leather, 
    and slim-cut textiles. Patterns are minimal. Categories include suits, jackets, and slim 
    silhouettes. Appeals to youth-driven, minimalist audiences.""",

    "Gucci by Tom Ford": """Polished sensual minimalism. Uses velvet, silk, leather, and 
    metallic finishes. Patterns are sleek or animal-inspired. Categories include tailoring, 
    eveningwear, and statement accessories. Appeals to confident, glamorous consumers.""",

    "Hermes by Maison Margiela":"""Intellectual quiet luxury. Materials include fine leather, cashmere,
    silk, and wool. Patterns are minimal. Categories include timeless tailoring and accessories. 
    Appeals to discerning, understated luxury buyers.""",

    "A.F Vandervorst": """Conceptual minimalism with military influence. Materials include structured 
    cotton, wool, and leather. Patterns are restrained. Categories include utilitarian tailoring and 
    outerwear. Appeals to design-focused minimalists.""",

    "Leon Emmanuel Blanck": """Extreme experimental tailoring. Uses heavy cotton, leather, and 
    technical blends. Patterns absent; focus on construction. Categories include engineered 
    outerwear and trousers. Appeals to avant-garde purists.""",

    "Maison Margiela": """Deconstruction and conceptual experimentation. Materials include repurposed 
    textiles, leather, and unconventional fabrics. Patterns are secondary to construction. Categories 
    include tailored garments and conceptual pieces. Appeals to intellectual fashion audiences.""",

    "Alexander MyQueen": """Dark romantic tailoring with theatrical intensity. Materials include structured 
    wool, silk, and embellished textiles. Patterns include dramatic motifs. Categories include sharp 
    tailoring and couture-inspired garments. Appeals to emotionally expressive wearers.""",

    "Balmain": """Power-driven glamour. Materials include structured wool, leather, and embellishments. 
    Patterns emphasize symmetry and bold detailing. Categories include sharp tailoring and statement 
    pieces. Appeals to confident luxury consumers.""",

    "Mugler":"""Futuristic sensuality with sculptural silhouettes. Materials include latex, 
    synthetics, and structured fabrics. Patterns are bold and graphic. Categories include 
    body-conscious dresses and statement pieces. Appeals to performance-driven, bold audiences.""" }

def make_designer_df() -> pd.DataFrame:
    """Return a DataFrame with designers as index and a single 'Description' column."""
    return pd.DataFrame(
        data=designer_dna.values(),
        index=designer_dna.keys(),
        columns=["Description"],
    )


