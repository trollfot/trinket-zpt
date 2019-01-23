import os
import curio
from functools import partial
from pathlib import Path
from chameleon.zpt import template


class Template:
    """Base class for any sort of page template
    """
    formats = {
        "file": template.PageTextTemplateFile,
        "inline": template.PageTextTemplate,
    }

    def __init__(self, body, mode="file", **kws):
        factory = self.formats.get(mode)
        self._template = factory(body, **kws)

    def __repr__(self):
        return '<Template %r>' % self.__class__.__name__

    def render(self, target_language=None, **namespace):
        namespace['target_language'] = target_language
        return self._template.render(**namespace)

    async def render_async(self, target_language=None, **namespace):
        renderer = partial(self.render, target_language=None, **namespace)
        return await curio.run_in_thread(renderer)
            

class TALTemplate(Template):

    formats = {
        "file": template.PageTemplateFile,
        "inline": template.PageTemplate,
    }

    @property
    def macros(self):
        return self._template.macros
    

class ZPTExtension:

    __slots__ = ('loader', 'environment')

    def __init__(self, cache: str=None):
        if cache is not None:
            cache = Path(cache)
            assert cache.is_dir()
            os.environ['CHAMELEON_CACHE'] = str(cache)

    def __getitem__(self, path: str):
        path = Path(path)
        if not path.is_file():
            raise LookupError(f'Template file {path} does not exist.')
        return TALTemplate(path)

    def template(self, path: str):
        template = self[path]
        return template.render_async
