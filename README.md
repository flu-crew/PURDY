# Introduction
Welcome to the GitHub repository and manual for the software PURDY!  PURDY stands for **P**ractical **U**tility for **R**ead **D**emultiplexing and assembl**Y** and is a fast and easy-to-use bash pipeline for MinION Influenza A sequences from any host and all gene segments that utilizes existing tools to perform demultiplexing and assembly, collect and calculate basic assembly statistics, generate phylogenetic trees alongside reference sequences, and classify swine HA sequences. PURDY is protected by a XXXXX liscence. Please cite XXXXX any time you present results generated using PURDY especially in a peer-reviewed publication. The aforementioned manuscript is also an important place to gain a complete understanding of the software and reading it is our recommended first step before using PURDY.

# How to Run PURDY
PURDY is a bash script that relies on a great number of dependencies. For your convenience we have built a docker image which provides an isolated filesystem containing all required dependencies. We recommend that you take advantage of this by either using Docker directly or using Docker indirectly via Aptainer (formerly Singularity).

## 1) Download a Test Data Set
In our manuscript we used three test data sets to demonstrate the capabilities of PURDY. The same three data sets can be used for a first run of PURDY to ensure that it is properly working for you. Note that multiple runs of PURDY on the same data will not yield identical results, but should yield very similar results where real data is involved, as opposed to "junk" where sequencing failed for any reason. The best way to check if your run was successful is to check the output to see if PURDY claims each segment ran successfully (it will tell you directly if something failed) and to compare your phylogenetic tree to the one in the "Test Results" section of this repository. If you wish, you can skip this step and jump to step 2, "Install Dependencies and Run PURDY"

### The Human Data Set
The smallest test data set is the Human host H3N2 Influenza A data set from Wang et al. 2015 (https://www.frontiersin.org/articles/10.3389/fmicb.2015.00766/full). Data from which can be found at the European Nucleotide Archive under the accession PRJEB9812 (https://www.ebi.ac.uk/ena/browser/view/PRJEB9812). We used the 2D MinION basecalled fastq data, not the fast5 format data. Here its harder to tell what is true data because of low coverage but there is available data for barcodes 2,6,12,13,26,37,46,52,65,71,72,80,82,86, and 89 **This data set is the best choice for someone who wants a fast test.**

### The Swine Data Set
The second smallest test data set is the Swine host H1N1, H1N2, and H3N2 Influenza A data set from Rambo-Martin et al. 2020 (https://journals.asm.org/doi/full/10.1128/msphere.00822-19). This data has already been demultiplexed and basecalled and can be found on NCBI under BioProject PRJNA528211. Search for the Bioproject then look for the link to the 13 SRA experiments if the provided link doesn't work. (https://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=528211). Here the true data is in barcodes 1,5,6,and 14-23. **This data set is the best choice for someone who wants a test with swine data of moderate size that can more accurately demonstrate the value of the classification function**

### The Avian Data Set
The largest test data set is the Avian host H5N1 Influenza A data set from Ip et al. 2023 (https://www.mdpi.com/2076-2607/11/2/529). This data can be downloaded frome ScienceBase (https://doi.org/10.5066/P93VXVGO). We used all three highly pathogenic H5N1 avian MinION sequences using the library assembly technique referred to as “Method A” in Ip et al. 2023. Here the true data is in barcodes and 4-6. **This data set is the best choice for someone who wants a large test data set with very deep coverage in an avian host**

## 2) Install Dependencies and Run PURDY
This section will guied you through how to install PURDY's dependencies and do a basic run. See the next section to explore available arguments.

### Using Docker
Docker is a container system wich allows you to run PURDY in an environment we created that already contains all the dependencies you need. For more information about Docker check out their website:
https://www.docker.com/
All you will need to make this work is to download docker to the machine you are using to run PURDY. You will find their download options here:
https://docs.docker.com/get-docker

If you are working on an HPC cluster you may be able to simply load a Docker module. On the other hand, some HPC systems believe Docker to be a security risk and therefore allow access to docker images only indirectly via Aptianer (formerly Singularity). If you are working an such an HPC systems try the "Using Aptainer" method of installing dependencies and running PURDY instead of this one.

We have uploaded the docker image to docker at https://hub.docker.com/repository/docker/darwin1990/purdydock/general

[Test and show direct examples]


### Using Aptainer (formerly Singularity)
[explain Aptianer]

singularity pull -F docker://darwin1990/purdydock
singularity run purdydock_latest.sif -t 12 -o fullPurdyRunOct18
[investigate whether this is really the best way post-Aptainer]



### Installing all Dependencies individually (not recommended)

# PURDY's Arguments (user options)
