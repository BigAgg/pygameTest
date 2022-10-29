# tiles.py

import pygame

tPath = "textures/Backgrounds/Tilesets/"


def getImg(p):
    return pygame.image.load(f"{tPath}{p}.png").convert()


def getRect(idxx, idxy, baseSizeidxx=16, baseSizeidxy=16, baseSizeW=16, baseSizeH=16):
    rect = pygame.Rect(idxx * baseSizeidxx, idxy * baseSizeidxy, baseSizeW, baseSizeH)
    return rect


tilesets = {}
allTextures = {}


def initialize():
    # loading in each tileset as surface
    pipes = getImg("Pipes")
    dungeon = getImg("TilesetDungeon")
    element = getImg("TilesetElement")
    field = getImg("TilesetField")
    floor = getImg("TilesetFloor")
    floorB = getImg("TilesetFloorB")
    floorDetail = getImg("TilesetFloorDetail")
    hole = getImg("TilesetHole")
    house = getImg("TilesetHouse")
    logic = getImg("TilesetLogic")
    nature = getImg("TilesetNature")
    relief = getImg("TilesetRelief")
    reliefDetail = getImg("TilesetReliefDetail")
    water = getImg("TilesetWater")
    interiorElements = getImg("Interior/Elements")
    interior = getImg("Interior/TilesetInterior")
    interiorFloor = getImg("Interior/TilesetInteriorFloor")
    interiorWallSimple = getImg("Interior/TilesetWallSimple")

    # importing tilesets into dictionary
    global tilesets
    tilesets = {
        "pipes": pipes,
        "dungeon": dungeon,
        "element": element,
        "field": field,
        "floor": floor,
        "floorB": floorB,
        "floorDetail": floorDetail,
        "hole": hole,
        "house": house,
        "logic": logic,
        "nature": nature,
        "relief": relief,
        "reliefDetail": reliefDetail,
        "water": water,
        "interiorElements": interiorElements,
        "interior": interior,
        "interiorFloor": interiorFloor,
        "interiorWallSimple": interiorWallSimple
    }

    # loading all textures
    global allTextures
    allTextures = {
        # pipes ------------------------------------------ pipes #
        # copper pipes vertical
        "cpvt": tile(1, getRect(0, 0), "pipes", "cpvt"),
        "cpvm": tile(1, getRect(0, 1), "pipes", "cpvm"),
        "cpvb": tile(1, getRect(0, 2), "pipes", "cpvb"),
        # copper pipes horizontal
        "cphl": tile(1, getRect(1, 0), "pipes", "cphl"),
        "cphm": tile(1, getRect(2, 0), "pipes", "cphm"),
        "cphr": tile(1, getRect(3, 0), "pipes", "cphr"),
        # copper pipes corner pieces
        "cpctl": tile(1, getRect(1, 1), "pipes", "cpctl"),
        "cpctr": tile(1, getRect(2, 1), "pipes", "cpctr"),
        "cpcbl": tile(1, getRect(1, 2), "pipes", "cpcbl"),
        "cpcbr": tile(1, getRect(2, 2), "pipes", "cpcbr"),
        # copper pipes t pieces
        "cptlrb": tile(1, getRect(3, 1), "pipes", "cptlrb"),
        "cptltr": tile(1, getRect(3, 2), "pipes", "cptltr"),
        "cptltb": tile(1, getRect(4, 1), "pipes", "cptltb"),
        "cptrtb": tile(1, getRect(4, 2), "pipes", "cptrtb"),
        # iron pipes vertical
        "ipvt": tile(1, getRect(5, 0), "pipes", "ipvt"),
        "ipvm": tile(1, getRect(5, 1), "pipes", "ipvm"),
        "ipvb": tile(1, getRect(5, 2), "pipes", "ipvb"),
        # iron pipes horizontal
        "iphl": tile(1, getRect(6, 0), "pipes", "iphl"),
        "iphm": tile(1, getRect(7, 0), "pipes", "iphm"),
        "iphr": tile(1, getRect(8, 0), "pipes", "iphr"),
        # iron pipes corner pieces
        "ipctl": tile(1, getRect(6, 1), "pipes", "ipctl"),
        "ipctr": tile(1, getRect(7, 1), "pipes", "ipctr"),
        "ipcbl": tile(1, getRect(6, 2), "pipes", "ipcbl"),
        "ipcbr": tile(1, getRect(7, 2), "pipes", "ipcbr"),
        # iron pipes t pieces
        "iptlrb": tile(1, getRect(8, 1), "pipes", "iptlrb"),
        "iptltr": tile(1, getRect(8, 2), "pipes", "iptltr"),
        "iptltb": tile(1, getRect(9, 1), "pipes", "iptltb"),
        "iptrtb": tile(1, getRect(9, 2), "pipes", "iptrtb"),
        # bamboo pipes vertical
        "bpvt": tile(1, getRect(10, 0), "pipes", "bpvt"),
        "bpvm": tile(1, getRect(10, 1), "pipes", "bpvm"),
        "bpvb": tile(1, getRect(10, 2), "pipes", "bpvb"),
        # bamboo pipes horizontal
        "bphl": tile(1, getRect(11, 0), "pipes", "bphl"),
        "bphm": tile(1, getRect(12, 0), "pipes", "bphm"),
        "bphr": tile(1, getRect(13, 0), "pipes", "bphr"),
        # bamboo pipes corner pieces
        "bpctl": tile(1, getRect(11, 1), "pipes", "bpctl"),
        "bpctr": tile(1, getRect(12, 1), "pipes", "bpctr"),
        "bpcbl": tile(1, getRect(11, 2), "pipes", "bpcbl"),
        "bpcbr": tile(1, getRect(12, 2), "pipes", "bpcbr"),
        # bamboo pipes t pieces
        "bptlrb": tile(1, getRect(13, 1), "pipes", "bptlrb"),
        "bptltr": tile(1, getRect(13, 2), "pipes", "bptltr"),
        "bptltb": tile(1, getRect(14, 1), "pipes", "bptltb"),
        "bptrtb": tile(1, getRect(14, 2), "pipes", "bptrtb"),
        # pipes ------------------------------------------ pipes #
        # dungeon ------------------------------------------ dungeon #
        # keystone bright
        "ksb": tile(4, getRect(0, 0), "dungeon", "ksb"),
        # keystone used
        "ksu": tile(4, getRect(1, 0), "dungeon", "ksu"),
        # buttons
        "buttonroundunused": tile(2, getRect(0, 1), "dungeon", "buttonroundunused"),
        "buttonroundused": tile(2, getRect(1, 1), "dungeon", "buttonroundused"),
        "buttonsquareunused": tile(2, getRect(2, 1), "dungeon", "buttonsquareunused"),
        "buttonsquareused": tile(2, getRect(3, 1), "dungeon", "buttonsquareused"),
        # trap
        "spiketrapon": tile(3, getRect(4, 1), "dungeon", "spiketrapon"),
        "spiketrapoff": tile(3, getRect(5, 1), "dungeon", "spiketrapoff"),
        # some interactives
        "undefinedcrystal": tile(1, getRect(7, 3), "dungeon", "undefinedcrystal"),
        "crystalgrey": tile(1, getRect(8, 3), "dungeon", "crystalgrey"),
        "crystalunused": tile(1, getRect(0, 2), "dungeon", "crystalunused"),
        "crystalblue": tile(1, getRect(1, 2), "dungeon", "crystablue"),
        "crystalred": tile(1, getRect(0, 3), "dungeon", "crystared"),
        "crystaorange": tile(1, getRect(1, 3), "dungeon", "crystalorange"),
        "flamepotlit": tile(4, getRect(2, 2), "dungeon", "flamepotlit"),
        "flamepotunlit": tile(4, getRect(2, 3), "dungeon", "flamepotunlit"),
        "switchred": tile(2, getRect(3, 3), "dungeon", "switchred"),
        "switchredpressed": tile(2, getRect(5, 3), "dungeon", "switchredpressed"),
        "switchblue": tile(2, getRect(4, 3), "dungeon", "switchblue"),
        "switchbluepressed": tile(2, getRect(6, 3), "dungeon", "switchbluepressed"),
        "globegrey": tile(4, getRect(3, 2), "dungeon", "globegrey"),
        "globelightblue": tile(4, getRect(4, 2), "dungeon", "globelightblue"),
        "globeblue": tile(4, getRect(5, 2), "dungeon", "globeblue"),
        "globered": tile(4, getRect(6, 2), "dungeon", "globered"),
        "globeorange": tile(4, getRect(7, 2), "dungeon", "globeorange"),
        # dungeon ------------------------------------------ dungeon #
        # element ------------------------------------------ element #
        "crate": tile(1, getRect(0, 0), "element", "crate"),
        "sack": tile(1, getRect(1, 0), "element", "sack"),
        "2posts": tile(1, getRect(2, 0), "element", "2posts"),
        "vase": tile(1, getRect(3, 0), "element", "vase"),
        "emptywoodbucket": tile(1, getRect(4, 0), "element", "emptywoodbucket"),
        "filledwoodbucket": tile(1, getRect(5, 0), "element", "filledwoodbucket"),
        "smallchestclosed": tile(4, getRect(6, 0), "element", "smallchestclosed"),
        "smallchestopened": tile(1, getRect(7, 0), "element", "smallchestopened"),
        "unwrittensign": tile(1, getRect(8, 0), "element", "unwrittensign"),
        "packedbarrel": tile(1, getRect(9, 0), "element", "packedbarrel"),
        "hocker": tile(1, getRect(11, 0), "element", "hocker"),
        "doghut": tile(1, getRect(12, 0), "element", "doghut"),
        "smallaltar": tile(1, getRect(14, 0), "element", "smallaltar"),
        "scarecrow": tile(1, getRect(15, 0), "element", "scarecrow"),
        "slimestatue1": tile(1, getRect(0, 1), "element", "slimestatue1"),
        "slimestatue2": tile(1, getRect(1, 1), "element", "slimestatue2"),
        "statuesocket": tile(1, getRect(2, 1), "element", "statuesocket"),
        "unusablechest": tile(1, getRect(3, 1), "element", "unusablechest"),
        "tonvasefat": tile(1, getRect(4, 1), "element", "tonvasefat"),
        "tonvasesmall": tile(1, getRect(5, 1), "element", "tonvasesmall"),
        "well": tile(1, getRect(6, 1), "element", "well"),
        "wellwithroof": tile(1, getRect(7, 1, baseSizeH=32), "element", "wellwithroof"),
        "foodbowl": tile(1, getRect(8, 1), "element", "foodbowl"),
        "loghocker": tile(1, getRect(9, 1), "element", "loghocker"),
        "bigsign": tile(1, getRect(11, 1, baseSizeW=48), "element", "bigsign"),
        "writtensign": tile(1, getRect(0, 2), "element", "writtensign"),
        "writtenframedsign": tile(1, getRect(1, 2), "element", "writtenframedsign"),
        "fatstatue": tile(1, getRect(2, 2), "element", "fatstatue"),
        "woodtombstone": tile(1, getRect(3, 2), "element", "woodtombstone"),
        "tombstone1": tile(1, getRect(4, 2), "element", "tombstone1"),
        "tombstone2": tile(1, getRect(5, 2), "element", "tombstone2"),
        "wellwithbucket": tile(1, getRect(6, 2), "element", "wellwithbucket"),
        "sandstone": tile(1, getRect(8, 2), "element", "sandstone"),
        "naturalwoodfence": tile(1, getRect(9, 2), "element", "naturalwoodfence"),
        "woodfence": tile(1, getRect(10, 2), "element", "woodfence"),
        "ropeon2poles": tile(1, getRect(11, 2, baseSizeH=32, baseSizeW=48), "element", "ropeon2poles"),
        "blueflagonrope": tile(1, getRect(14, 2, baseSizeH=32), "element", "blueflagonrope"),
        "redflagonrope": tile(1, getRect(15, 2, baseSizeH=32), "element", "redflagonrope"),
        "emptywoodcart": tile(1, getRect(0, 3, baseSizeH=32, baseSizeW=32), "element", "emptywoodcart"),
        "fullwoodcart": tile(1, getRect(2, 3, baseSizeH=32, baseSizeW=32), "element", "fullwoodcart"),
        "3crates": tile(1, getRect(4, 3, baseSizeH=32, baseSizeW=32), "element", "3crates"),
        "birdhouse": tile(1, getRect(6, 3, baseSizeH=32), "element", "birdhouse"),
        "hocker1": tile(1, getRect(7, 4), "element", "hocker1"),
        "ropeonfloor": tile(1, getRect(8, 3), "element", "ropeonfloor"),
        "stonegrave": tile(1, getRect(0, 5, baseSizeH=32), "element", "stonegrave"),
        "woodgrave": tile(1, getRect(1, 5, baseSizeH=32), "element", "woodgrave"),
        
    }


class tile(pygame.sprite.Sprite):
    def __init__(self, colissionLayer, srcRect, tileset: str, tileName, position=(0, 0)):
        super().__init__()
        size = srcRect.size
        surf = pygame.Surface(size)
        surf.blit(tilesets.get(tileset), (0, 0), srcRect)
        surf.set_colorkey((0, 0, 0))
        self.name = tileName
        self.colissionLayer = colissionLayer
        self.surf = surf
        self.srcR = srcRect
        self.basePos = position
        self.position = position
        # for testing only, remove when done
        self.tileset = tileset

    def draw(self, screen: pygame.Surface):
        self.srcR.center = self.position
        screen.blit(self.surf, self.srcR)

    def update(self, newPos):
        self.position -= newPos

    def initPos(self, newPos):
        self.position = newPos


class chunk(pygame.sprite.Sprite):
    def __init__(self, size: tuple, position: tuple, level):
        surf = pygame.Surface(size)
        colissionObjects = pygame.sprite.Group()
        for sprite in level:
            if sprite.colissionLayer > 0:
                surf.blit(sprite.surf, sprite.position - position)
            else:
                colissionObjects.add(sprite)
        self.surf = surf
        self.rect = surf.get_rect()
        self.rect.center = position
        self.basePos = position
        self.position = position
        self.colSprites = colissionObjects
        self.entities = pygame.sprite.Group()

    def draw(self, screen: pygame.Surface):
        screen.blit(self.surf, self.position)
        self.colSprites.draw(screen)

    def update(self, newPos: tuple):
        self.position = self.basePos - newPos
        self.colSprites.update(newPos)
        self.entities.update(newPos)
