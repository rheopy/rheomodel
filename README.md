# rheomodel

Collection of rheology flow curve models

## Library structure

* **models.bib** : ships with the library and is the bibtex file with the citation for the source of the model
* **models.py** : list of python function implementing each model expressed as stress as a function shear rate
* **function.py** : library functionality like showing model and citation table


```python
import rheomodel as rm
rm.library_to_table(rm.library)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>author</th>
      <th>title</th>
      <th>publisher</th>
      <th>year</th>
      <th>address</th>
      <th>journal</th>
      <th>volume</th>
      <th>number</th>
      <th>pages</th>
    </tr>
    <tr>
      <th>ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>newton_1687</th>
      <td>Isaac Newton</td>
      <td>Philosophiæ Naturalis Principia Mathematica</td>
      <td>Josephi Streater</td>
      <td>1687</td>
      <td>London</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>ostwald_1929</th>
      <td>Ostwald, Wilhelm</td>
      <td>Über die Geschwindigkeitsfunktion der Newton's...</td>
      <td>Walter de Gruyter</td>
      <td>1929</td>
      <td>NaN</td>
      <td>Zeitschrift für physikalische Chemie</td>
      <td>102</td>
      <td>1</td>
      <td>64--79</td>
    </tr>
    <tr>
      <th>bingham_1916</th>
      <td>Bingham, Eugene C.</td>
      <td>A new conception of plasticity and viscous flow</td>
      <td>Elsevier</td>
      <td>1916</td>
      <td>NaN</td>
      <td>The Journal of the Franklin Institute</td>
      <td>181</td>
      <td>6</td>
      <td>543--552</td>
    </tr>
    <tr>
      <th>herschel_bulkley_1926</th>
      <td>Herschel, Winslow Hobart and Bulkley, Robert</td>
      <td>Measurement of consistency as applied to rubbe...</td>
      <td>American Society for Testing and Materials</td>
      <td>1926</td>
      <td>NaN</td>
      <td>Proceedings of the American Society for Testin...</td>
      <td>26</td>
      <td>2</td>
      <td>621--633</td>
    </tr>
    <tr>
      <th>carreau_yasuda_1979</th>
      <td>Carreau, Pierre J. and Yasuda, Koichi</td>
      <td>Rheological equations from molecular network t...</td>
      <td>Wiley</td>
      <td>1979</td>
      <td>NaN</td>
      <td>Journal of Polymer Science</td>
      <td>11</td>
      <td>2</td>
      <td>371--388</td>
    </tr>
    <tr>
      <th>cross_1925</th>
      <td>Cross, Malcolm M.</td>
      <td>Viscosity of Colloids</td>
      <td>ACS Publications</td>
      <td>1925</td>
      <td>NaN</td>
      <td>The Journal of Physical Chemistry</td>
      <td>29</td>
      <td>11</td>
      <td>1409--1426</td>
    </tr>
    <tr>
      <th>caggioni2020variations</th>
      <td>Caggioni, Marco and Trappe, Veronique and Spic...</td>
      <td>Variations of the Herschel--Bulkley exponent r...</td>
      <td>AIP Publishing</td>
      <td>2020</td>
      <td>NaN</td>
      <td>Journal of Rheology</td>
      <td>64</td>
      <td>2</td>
      <td>413--422</td>
    </tr>
  </tbody>
</table>
</div>




```python
!jupyter nbconvert --to markdown README.ipynb
```

    [NbConvertApp] Converting notebook README.ipynb to markdown
    [NbConvertApp] Writing 4174 bytes to README.md
    


```python

```
