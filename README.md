# Similarity search in ChEMBL

Given a molecule, this model looks for its 100 nearest neighbors in the ChEMBL database, according to ECFP4 Tanimoto similarity. Due to size constraints, the model redirects queries to the ChEMBL server, so when using this model predictions are posted online.

## Identifiers

* EOS model ID: `eos2a9n`
* Slug: `chembl-similarity`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Generative`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `List`
* Interpretation: List of 100 nearest neighbors

## References

* [Publication](https://www.frontiersin.org/articles/10.3389/fchem.2020.00046/full)
* [Source Code](http://130.92.106.217:8080/chemblMuti.v1/)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Citation

If you use this model, please cite the [original authors](https://www.frontiersin.org/articles/10.3389/fchem.2020.00046/full) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!