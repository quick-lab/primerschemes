# primerschemes

Central machine-readable repo for newly generated PrimerSchemes and PrimalPanels

For a user-navigable version please go [here](https://labs.primalscheme.com)


## Quick Start

Each version of a primerscheme has three parts; `{schemename}/{ampliconsize}/{version}`, which when combined form the scheme's unique identifier.

For a scheme to be added to the repo it requires three essential files. 
- `primer.bed`: Contains the primer information.   
- `reference.fasta`: Contains the reference genomes.
- `info.json`: Contains key metadata for the scheme.

The `primal-page create` command will generate the `info.json` and parses a bed file and a fasta file into `primer.bed` and `reference.fasta`

Additional files are copied into the schemes work directory. 

> See [primal-page](https://github.com/ChrisgKent/primal-page) for more details.

## What does part each mean?

### schemename

The family of scheme.

The naming format is flexible, but we encourage the form of {group}-{target}. For example `artic-sars-cov2`
- Follow good scientific naming practices. No places. No vague names (`sar2`)


### ampliconsize

The amplicon size of the scheme in nucleotides. PCR products typically are ± 10%. Shorter schemes (400bp) generally are more sensitive, down to Ct 35+, compared to larger schemes (2000bp), down to Ct 30.

### version 

The version of the scheme. This follows the format of `vz.y.x-abc`. 
Selecting the correct version is vital for wet lab work and bioinformatic analysis. 

- `z`: represents a total resigned of a scheme. 

- `y`: represents a change in primers to an existing scheme. Ie adding spike in primers to account for new mutations. 

- `x`: represents a change in the primer concentration used. No change to the primer sequences. 

- `-abc`: an optional suffix to represent a scheme being remapped to a new reference genome. No changes to the primer sequences or concentration. 

#### Examples 

`v2.0.0` is an entirely different scheme to `v1.0.0`. 

`v1.0.0` has two additional primers added to account for a new mutation. The new scheme would be `v1.1.0`

`v1.1.0` has primer concentrations changed to improve even coverage of amplicons. The new scheme would be `v1.1.1`  

`v1.0.0` has identical primers (sequence and concentration) to `v1.0.0-alpha`. However, the primers will now be mapped to the `alpha` reference genome.