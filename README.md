# primerschemes

Central machine readable repo for newly generated PrimerSchemes and PrimalPanels

For a user navigable version please go [here](https://labs.primalscheme.com)


## Quick Start

Each version of a primerscheme has three parts; `{schemename}/{ampliconsize}/{version}`, which when combined these form the schemes unique identifier.

For a scheme to be added to the repo it requires three essental files. 
- `primer.bed`: Contains the primer infomation.   
- `reference.fasta`: Contains the reference genomes.
- `info.json`: Contains key metadata for the scheme.

The `primal-page create` command will generates the `info.json` and parses a bed file and a fasta file into `primer.bed` and `reference.fasta`

Additional files are copied into the schemes work directory. 

> See [primal-page](https://github.com/ChrisgKent/primal-page) for more details.


------------------------------------------------------------------------

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/) 

![](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)
