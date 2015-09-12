@extends("base.tpl")

@def mtitle():
   iii Welcome name 
@end

@def hello():
    <h1>Hello   kjlkjlk</h1>
@end

@def cont():
    @(
       x = 'Hy'
       import time
       t = time.time()
    )
    <H1>It'time @x  @t!s</H1>
@end

@def contenu(x):
    <h1>HomeiU @x!s</h1>
    <p>
        Welcome to My Site!
    </p>
@end


@def footer():
    @(
        import urllib2
        data =  "Hello"
    )
    <h1>Footer  @data</h1>
@end

@def pied():
   <h1>Pied</h1>
@end
