=======================
Trinket templating: ZPT
=======================

*******
Example
*******

.. code-block:: python

   from trinket import Trinket, Response          
   from trinket_zpt import zpt
   from pathlib import Path
   
   bauble = zpt(Trinket(), cache='/tmp')
   
   @bauble.route('/page')
   async def page_with_zpt_template(request):
       template = bauble['zpt'].template(
           Path(__file__).parent / Path('test.pt'))
       html = await template(title='Curio HTTP Server', name='Trinket')
       return Response.html(html)
   
   bauble.start()
