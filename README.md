# Fintual-Desaf-o-para-Postular

En el archivo `portfolio.py` se puede encontrar la implementación de la clase _Portfolio_ como así también una función auxiliar que sería necesaria para poder implementar el método _profit_ de la manera planteada.

La clase y los métodos implementados buscan resolver la siguiente consigna:

> Construct a simple _Portfolio_ class that has a collection of _Stocks_ and a _Profit_ method that receives 2 dates and returns the profit of the _Portfolio_ between those dates.
> Assume each _Stock_ has a _Price_ method that receives a date and returns its price.
> Bonus Track: make the _Profit_ method return the **_annualized return_** of the portfolio between the given dates.

## Atributos

La clase _Portfolio_ cuenta con un atributo _Stocks_ que es un diccionario donde cada clave es una _Stock_ y su valor correspondiente, _quantity_, la cantidad de acciones de esa instancia que tiene el _Portfolio_.

## Métodos

### _Instanciar el Portfolio_

El método _init_ genera un diccionario vacío, pero si el objeto de tipo _Portfolio_ se instancia con el _Class method_ _portfolio_with_stocks_, se obtiene un _Portfolio_ con el diccionario de la forma **{_stock_: _quantity_}** que se pase como argumentos.

### _Agregar y quitar Stocks_

También cuenta con un método que permite agregar o quitar _Stocks_ al portfolio. Dicho método, además de requerir un _Stock_, toma por parámetro una _quantity_: si la _quantity_ es igual o mayor a cero, se suma al _valor_ cuya _clave_ es la _Stock_ ingresada (si no existe esa _Stock_ en el _Portfolio_ se añade el par (_Stock_, _quantity_) al _Portfolio_); si la _quantity_ es negativa, se resta al _valor_ cuya _clave_ es la _Stock_ ingresada (aunque esa resta no puede dar un resultado menor a cero, de forma que se levantaría una _exception_).

### _Obtener ganancias anualizadas_

El método _profit_ está implementado de forma tal de cumplir con el _bonus track_ de la consigna. El resultado está expresado en porcentaje. Está pensado para que las _dates_ ingresadas sean del tipo _string_, aunque para su implementación real debería tenerse en cuenta el _tipo_ del parámetro del método _price_ de la clase _Stock_. La ecuación utilizada para calcular la **_annualized_profit_** se obtuvo del siguiente link: https://www.investopedia.com/terms/a/annualized-total-return.asp . En este método llama una función auxiliar que obtiene la diferencia en días (devuelve un _int_) entre dos fechas pasadas como _string_ en formato 'YY-MM-DD'. Esta función no debería estar implementada en este módulo, pero para que se entiendiera la idea decidí agregarla.
