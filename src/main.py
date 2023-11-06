from level import Level
from engine import Engine

level = Level((5, 5))
engine = Engine()
engine.on("render", level.render)
engine.on("tick", level.tick)
engine.on("keydown", level.handleKeyDown)
engine.start()