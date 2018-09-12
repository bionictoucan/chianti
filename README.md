# Chianti Lines
A simple file to easily find the corresponding ion for a certain wavelength in the CHIANTI database and vice versa. This uses Python 3 and can easily be done from the interpreter or a Jupyter notebook.

All that is needed is to download the chianti_db.pkl file but the source code is here for transparency.

To use the file:

```
import pickle

with open("chianti_db.pkl", "rb") as input:
    ch = pickle.load(input)
```

The line database is now contained in the class object we have called ```ch```. To get the complete list of either ions or wavelengths, the attributes of the class can be accessed via

```
ch.ions
ch.wvls
```

respectively. To find the ion corresponding to the wavelength of interest (within the range 1-600000&#8491;), simply use the following class method after loading the pickle:

```
ch.getIon(wavelength)
```

where ```wavelength``` can be given as a number in Angstroms within this wavelength range. To find all of the wavelengths emitted by a specific ion, use the following class method:

```
ch.getWavelengths(ion)
```

where ```ion``` is a string representing the shorthand for expressing the ion of interest, e.g. singly-ionised aluminium would be "AlII", 17 times ionised nickel would be "NiXVIII" etc..
