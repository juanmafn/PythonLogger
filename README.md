# PythonLogger

## Cómo usarlo

### 1. Importa la librería

```python
from Log import Log
```

### 2. Instancia la clase Log

###### Le pasamos un nombre del contexto en el que estemos

```python
log = Log("Context name")
```

###### Si estamos en una clase, podemos inicializarlo de esta forma:


```python
def __init__(self):
  self.log = Log(self.__class__.__name__)
```

### 3. Usar

###### Tenemos 8 tipos diferentes de logs

```python
log.Enter(message)
log.Exit(message)
log.Info(message)
log.Trace(message)
log.Debug(message)
log.Warn(message)
log.Error(message)
log.Fatal(message)
```
