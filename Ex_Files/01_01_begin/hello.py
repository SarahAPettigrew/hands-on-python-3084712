import this

try:
    import camelcas

    c = camelcase.CamelCase()
    txt = 'this is some text'
    assert isinstance(txt, str)
    t = [5, 6] * (4,)
    print(y.hump(txt))

except NameError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except ImportError as e:
    print(e)

finally:
    print("done")
