init python in gui:
    def button_properties(kind):
        g = globals()

        def get(prop):
            if kind + "_" + prop in g:
                return g[kind + "_" + prop]

            return None

        borders = get("borders")

        tile = get("tile")
        if tile is None:
            tile = button_tile

        backgrounds = [ ]

        if kind != "button":
            backgrounds.append("00sanpy/gui/button/" + kind[:-7] + "_[prefix_]background" + button_image_extension)

        backgrounds.append("00sanpy/gui/button/[prefix_]background" + button_image_extension)

        if renpy.variant("small"):
            backgrounds = [ i.replace("00sanpy/gui/button", "00sanpy/gui/phone/button") for i in backgrounds ] + backgrounds

        rv = {
            "background" : Frame(backgrounds, borders or button_borders, tile=tile),
        }

        if borders is not None:
            rv["padding"] = borders.padding

        width = get("width")
        height = get("height")

        if width is not None:
            rv["xsize"] = width

        if height is not None:
            rv["ysize"] = height

        return rv
