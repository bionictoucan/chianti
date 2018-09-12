class chiantiIons():
    '''
    Parameters
    ----------
    ionList : list
        The list of the ions in CHIANTI.
    wvlList : list
        The list of the wavelengths corresponding to the ions.
    '''
    def __init__(self,ionList,wvlList):
        self.ions = ionList
        self.wvls = [float(i) for i in wvlList]

    def __repr__(self):
        return "An object containing the complete list of CHIANTI ions and their corresponding wavelengths (in Angstroms) ordered by increasing wavelength."

    def getIon(self,wvl):
        '''
        A class method to get the ion associated with the specified wavelength.

        Parameters
        ----------
        wvl : str
            The wavelength of the emission of the ion in Angstroms.

        Returns
        -------
        str
            The ion that emitted a photon at the wavelength in question.
        '''

        idx = min(enumerate(self.wvls),key=lambda x: abs(x[1]-wvl))[0] #returns only the index corresponding to the closest wavelength

        return self.ions[idx]

    def getWavelengths(self,ion):
        '''
        A class method to get the wavelengths in Angstroms associated with a particular ion (may return >1 wavelength for different transitions).

        Parameters
        ----------
        ion : str
            The ion whose emission lines the user would like to see.
        
        Returns
        -------
        lst : list
            A list of the wavelengths emitted by the ion in question.
        '''

        idxs = [x for x,y in enumerate(self.ions) if y == ion]
        lst = []

        for z in idxs:
            lst.append(self.wvls[z])

        return lst