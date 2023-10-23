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

### Using Apptainer (most recommended, formerly Singularity)
Without going into details Apptainer is a more secure method of running containers on an HPC system and you can learn more about it here: https://apptainer.org/docs/user/main/index.html
To upload the docker image via Apptainer simply run this command:
singularity pull -F docker://darwin1990/purdydock

This will install the file, "purdydock_latest.sif", in the directory where this command was run.

And then To run PURDY run this command:
```
singularity run purdydock_latest.sif
```

This would run PURDY with all default arguments. A more realistic example is the following:
```
singularity run purdydock_latest.sif -t 12 -o fullPurdyRunOct19
```

Everything folloving "purdydock_latest.sif" is fed directly to PURDY. In this case "-t 12" tells PURDY to use 12 threads and "-o fullPurdyRunOct19" tells PURDY to put the results in a folder called "fullPurdyRunOct19" which will be created if one does not already exist.

### Using Docker
Docker is a container system wich allows you to run PURDY in an environment we created that already contains all the dependencies you need. For more information about Docker check out their website: https://www.docker.com/
All you will need to make this work is to download docker to the machine you are using to run PURDY. You will find their download options here: https://docs.docker.com/get-docker

If you are working on an HPC cluster you may be able to simply load a Docker module. On the other hand, some HPC systems believe Docker to be a security risk and therefore allow access to docker images only indirectly via Apptianer (formerly Singularity). If you are working an such an HPC systems try the "Using Aptainer" method of installing dependencies and running PURDY instead of this one.

We have uploaded the docker image to docker at https://hub.docker.com/repository/docker/darwin1990/purdydock/general

To run PURDY using Docker directly first make sure that docker is installed and running, go to the directory where your data is stored, then load the docker image in using the command: 
```
docker pull darwin1990/purdydock
```

Then create the input and output folders. For now the input folder must be named "fastq_pass" and contain all the fastq files you want to be part of this run. This will be changed very soon in an update. If you're using Docker directly rather than Apptainer you will have to create a folder for the output even if you are using the default output folder, "fastq_pass_Demultiplexed", for Docker to see your input and write an output to a place where you can access it.
```
mkdir fastq_pass
mv [your_data.fastq] fastq_pass

mkdir fastq_pass_Demultiplexed
docker run -v "$(pwd)/fastq_pass":"/fastq_pass" -v "$(pwd)/fastq_pass_Demultiplexed":"/fastq_pass_Demultiplexed" darwin1990/purdydock
```

Here [your_data] is a stand-in for all of your fastq-files you want ot be part of this run. This would run PURDY with all default arguments. A more realistic example is the following:

```
mkdir fastq_pass
mv [your_data.fastq] fastq_pass

mkdir fullPurdyRunOct19
docker run -v "$(pwd)/fastq_pass":"/fastq_pass" -v "$(pwd)/testRunOct23":"/testRunOct23" darwin1990/purdydock -t 6 -o testRunOct19
```

In this case "-t 6" tells PURDY to use 6 threads and "-o fullPurdyRunOct19" tells PURDY to put the results in a folder called "fullPurdyRunOct19" which will be created if one does not already exist.

### Installing all Dependencies individually (not recommended)
While it is possible to install all of PURDY's dependencies without the docker image it is not recommended. The total number of dependencies is great and there are sometimes conflicts between versions of software which can be hard to predict.  If you choose to take this route despite this warning here are the dependencies you will need to install (some of which have their own dependencies):

Guppy - https://help.nanoporetech.com/en/collections/3738249-guppy

IRMA (using the flu module) - https://wonder.cdc.gov/amd/flu/irma/

R - https://www.r-project.org/

perl - https://www.perl.org/get.html

samtools - http://www.htslib.org/

MAFFT - https://mafft.cbrc.jp/alignment/software/

FastTree - http://www.microbesonline.org/fasttree/

Python3 - https://www.python.org/downloads/


# PURDY's Arguments (user options)
