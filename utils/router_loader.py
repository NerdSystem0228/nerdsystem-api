import glob
from importlib import import_module
from .logger import logger
def load_routers(app, module):
    for i in glob.glob("routers/**/*.py", recursive=True):
        if "__init__.py" in i:
            continue
        try:
            router=import_module(f"{i.replace('/', '.')[:-3]}")
            app.include_router(router.router)
            logger.info(f"Loaded Router: {i}")
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            logger.error(
                f"Failed to load Router {i}\n{exception}"
            )  