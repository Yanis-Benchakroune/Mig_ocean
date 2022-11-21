import numpy as np
import matplotlib.pyplot as plt

dico = {"R" : "PSF\PSF_10cm_512x512_B1_GSD_2.8m.dat",
        "G" : "PSF\PSF_10cm_512x512_B2_GSD_2.8m.dat",
        "B" : "PSF\PSF_10cm_512x512_B3_GSD_2.8m.dat",
        "IR" : "PSF\PSF_10cm_512x512_MIR_GSD_2.8m.dat",
        "pan" : "PSF\PSF_10cm_512x512_Pa_GSD_0.7m.dat"}

def psf(s):
    """
    Entrée :
        s : string
            nom de la bande ("R", "G", "B", "IR" ou "pan")
    Sortie :
        psf : tableau numpy de taille 512x512
            matrice de la PSF de la bande donnée
    """

    mat_psf = np.empty((512, 512))
    i = 0

    with open(dico[s], 'r') as f:
        for line in f:
            mat_psf[i] = line.rstrip("\n").lstrip("   ").split("   ")
            i += 1
        
    mat_psf = mat_psf.astype(float)
    return mat_psf

plt.imshow(psf("R"))
plt.show()