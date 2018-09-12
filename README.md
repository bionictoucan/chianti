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

where ```ion``` is a string representing the shorthand for expressing the ion of interest, e.g. singly-ionised aluminium would be "AlII" (looks bad in this font but it should be Al II without a space), 17 times ionised nickel would be "NiXVIII" etc..

There is also a Jupyter Notebook that can be downloaded (chianti.ipynb) for quick and interactive use of this database.

## References
"CHIANTI - an atomic database for emission lines", Dere, K. P.; Landi, E.; Mason, H. E.; Monsignori Fossi, B. C.; Young, P. R., *Astronomy and Astrophysics*, 1997, [ADS Link](http://adsabs.harvard.edu/cgi-bin/nph-bib_query?bibcode=1997A%26AS..125..149D&db_key=AST&high=32ac1ec07715657)

"CHIANTI - An atomic database for emission lines. Version 8", Del Zanna, G.; Dere, K. P.; Young, P. R.; Landi, E.; Mason, H. E., *Astronomy and Astrophysics*, 2015, [ADS Link](http://adsabs.harvard.edu/abs/2015A%26A...582A..56D)
