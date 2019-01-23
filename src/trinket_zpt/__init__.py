from pathlib import Path
from trinket_zpt.extension import ZPTExtension


def zpt(app, cache: str=None):
    if cache is not None:
        cache = Path(cache)
    app['zpt'] = ZPTExtension(cache)
    return app
