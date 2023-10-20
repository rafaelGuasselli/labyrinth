from level import Level
from engine import Engine

level = Level((5, 5))
engine = Engine()
engine.on("render", level.render)
engine.on("keydown", level.handleKeyDown)

engine.setFps(30)
engine.start()