from level import Level
from engine import Engine

level = Level((5, 5))
engine = Engine()
engine.setFps(30)

engine.on("exit", engine.stop)
engine.on("render", level.render)
engine.on("keydown", level.handleKeyDown)
engine.start()