init python:

    def MaxScale(img, minwidth=config.screen_width, minheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(minwidth) / currwidth
        yscale = float(minheight) / currheight

        if xscale > yscale:
            maxscale = xscale
        else:
            maxscale = yscale

        return im.FactorScale(img, maxscale, maxscale)

    def MinScale(img, maxwidth=config.screen_width, maxheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(maxwidth) / currwidth
        yscale = float(maxheight) / currheight

        if xscale < yscale:
            minscale = xscale
        else:
            minscale = yscale

        return im.FactorScale(img, minscale, minscale)

    maxnumx = 2
    maxnumy = 2
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0


    class GalleryItem:
        def __init__(self, name, images, thumb, locked="lockedthumb"):
            self.name = name
            self.images = images
            self.thumb = thumb
            self.locked = locked
            self.refresh_lock()

        def num_images(self):
            return len(self.images)

        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            for img in self.images:
                if not renpy.seen_image(img):
                    lockme = True
                else:
                    self.num_unlocked += 1
            self.is_locked = lockme


    gallery_items = []
    gallery_items.append(GalleryItem("Capitulo1", ["cg1"], "thumb1")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg2"], "thumb2")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg3"], "thumb3")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg4"], "thumb4")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg5"], "thumb5")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg6"], "thumb6")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg7"], "thumb7")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg8"], "thumb8")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg9"], "thumb9")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg10"], "thumb10")) # Ok
    gallery_items.append(GalleryItem("Capitulo1", ["cg11"], "thumb11")) # Ok
