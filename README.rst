====
chop
====

.. image:: https://anaconda.org/fi0/c3dp/badges/version.svg   
        :target: https://anaconda.org/fi0/chop
        
.. image:: https://img.shields.io/pypi/v/chop.svg
       :target: https://pypi.org/project/chop3/

.. image:: https://readthedocs.org/projects/venus-chopper-design/badge/?version=latest
        :target: https://venus-chopper-design.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status
     




Produce the time distance diagram for different chopper configuration
---------------------------------------------------------------------------------
Features
--------

* Calculation of the band-width to avoid frame overlap
* Calculation of the time when chopper T1 or T2  or T3 opens
* Calculation of the chopper phase angle
* Plot the time-distance diagram for chopper configuration


Examples
--------
see notebook : https://github.com/ornlneutronimaging/chop/blob/master/notebooks/Time_Distance_DIagram-Fahima.ipynb

.. image:: https://raw.githubusercontent.com/ornlneutronimaging/chop/master/figure/Screenshot%20from%202019-06-11%2009-06-13.png
   :width: 300pt


Installation
-------------
* Clone the repository and execute from within and execute:

.. code-block:: shell

    $ git clone git@github.com:ornlneutronimaging/chop.git
    $ cd chop
    
* Anaconda (Recommended)
.. code-block:: shell

    $ conda install -c fi0 chop
    
* Pypi
.. code-block:: shell

    $ pip install chop3
    



