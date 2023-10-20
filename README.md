# Introduction
Welcome to the GitHub repository and manual for the software PURDY!  PURDY stands for **P**ractical **U**tility for **R**ead **D**emultiplexing and assembl**Y** and is a fast and easy-to-use bash pipeline for MinION Influenza A sequences from any host and all gene segments that utilizes existing tools to perform demultiplexing and assembly, collect and calculate basic assembly statistics, generate phylogenetic trees alongside reference sequences, and classify swine HA sequences. PURDY is protected by a XXXXX liscence. Please cite XXXXX any time you present results generated using PURDY especially in a peer-reviewed publication. The aforementioned manuscript is also an important place to gain a complete understanding of the software and reading it is our recommended first step before using PURDY.

# How to Run PURDY
PURDY is a bash script that relies on a great number of dependencies. For your convenience we have built a docker image which provides an isolated filesystem containing all required dependencies. We recommend that you take advantage of this by either using Docker directly or using Docker indirectly via Aptainer (formerly Singularity). 

## Available Test Data Sets
In our manuscript we used three test data sets to demonstrate the capabilities of PURDY. The same three data sets can be used for a first run of PURDY to ensure that it is properly working for you. Note that multiple runs of PURDY on the same data will not yield identical results, but should yield very similar results where real data is involved, as opposed to "junk" where sequencing failed for any reason. The best way to check if your run was successful is to check the output to see if PURDY claims each segment ran successfully (it will tell you directly if something failed) and to compare your phylogenetic tree to the one in the "Test Results" section of this repository. 

### The Human Data Set
The smallest test data set is the Human host Influenza A data set from Wang et al. 2015 (https://www.frontiersin.org/articles/10.3389/fmicb.2015.00766/full). Data from which can be found at the European Nucleotide Archive under the accession PRJEB9812 (https://www.ebi.ac.uk/ena/browser/view/PRJEB9812). We used the 2D MinION basecalled fastq data, not the fast5 format data. **This data set is the best choice for someone who wants a fast test.**

### The Swine Data Set
The second smallest test data set is the Swine host Influenza A data set from Rambo-Martin et al. 2020 (https://journals.asm.org/doi/full/10.1128/msphere.00822-19). This data has already been demultiplexed and basecalled and can be found on NCBI under BioProject PRJNA528211. Search for the Bioproject then look for the link to the 13 SRA experiments if the provided link doesn't work. (https://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=528211). **This data set is teh best choice for someone who wants a test with swine data that can more accurately demonstrate the value of the classification function**

### The Avian Data Set
The largest test data set is the Avian host Influenza A data set from Ip et al. 2023 (https://www.mdpi.com/2076-2607/11/2/529). 



## Using Docker

## Using Aptainer (formerly Singularity)

## Installing all Dependencies individually (not recommended)

# PURDY's Arguments (user options)
