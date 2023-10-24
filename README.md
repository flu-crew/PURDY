# Introduction
Welcome to the GitHub repository and manual for the software PURDY!  PURDY stands for **P**ractical **U**tility for **R**ead **D**emultiplexing and assembl**Y** and is a fast and easy-to-use bash pipeline for Oxford Nanopore Technologies (ONT) Influenza A sequences from any host and all gene segments that utilizes existing tools to perform demultiplexing and assembly, collect and calculate basic assembly statistics, generate phylogenetic trees alongside reference sequences, and classify swine HA sequences. PURDY is protected by a version 3 of the GNU General Public liscence Which can be found on this repository. If you have any questions about appropriate use of this softwore please read the liscence, but in short it states that if you use PURDY and report on the rusults you have a responsibility to cite our peer-reviewed manuscript XXXXX. The aforementioned manuscript is an important place to gain a complete understanding of the software and reading it is our recommended first step before using PURDY.

# How to Run PURDY
PURDY is a bash script that relies on a great number of dependencies. For your convenience we have built a docker image which provides an isolated filesystem containing all required dependencies. We recommend that you take advantage of this by either using Docker directly or using Docker indirectly via Apptainer (most recommended; formerly Singularity).

## 1) Download a Test Data Set
In our manuscript we used three test data sets to demonstrate the capabilities of PURDY. The same three data sets can be used for a first run of PURDY to ensure that it is properly working for you. Note that multiple runs of PURDY on the same data will not yield identical results, but should yield very similar results where real data is involved, as opposed to "junk" where sequencing failed for any reason. The best way to check if your run was successful is to check the output to see if PURDY claims each segment ran successfully (it will tell you directly if something failed) and to compare your phylogenetic tree to the one in the "Test Results" section of this repository. If you wish, you can skip this step and jump to step 2, "Install Dependencies and Run PURDY" and run PURDY first on your data.

### The Human Data Set
The smallest test data set is the Human host H3N2 Influenza A data set from Wang et al. 2015 (https://www.frontiersin.org/articles/10.3389/fmicb.2015.00766/full). Data from which can be found at the European Nucleotide Archive under the accession PRJEB9812 (https://www.ebi.ac.uk/ena/browser/view/PRJEB9812). We used the 2D MinION basecalled fastq data, not the fast5 format data. Here its harder to tell what is true data because of low coverage but there is available data for barcodes 2,6,12,13,26,37,46,52,65,71,72,80,82,86, and 89 **This data set is the best choice for someone who wants a fast test.**

### The Swine Data Set
The second smallest test data set is the Swine host H1N1, H1N2, and H3N2 Influenza A data set from Rambo-Martin et al. 2020 (https://journals.asm.org/doi/full/10.1128/msphere.00822-19). This data has already been demultiplexed and basecalled and can be found on NCBI under BioProject PRJNA528211 (https://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=528211). Search for the Bioproject then look for the link to the 13 SRA experiments if the provided link doesn't work. Here the true data is in barcodes 1,5,6,and 14-23. **This data set is the best choice for someone who wants a test with swine data of moderate size that can more accurately demonstrate the value of the classification function.**

### The Avian Data Set
The largest test data set is the Avian host H5N1 Influenza A data set from Ip et al. 2023 (https://www.mdpi.com/2076-2607/11/2/529). This data can be downloaded from ScienceBase (https://doi.org/10.5066/P93VXVGO). We used all three highly pathogenic H5N1 avian MinION sequences using the library assembly technique referred to as “Method A” in Ip et al. 2023 (https://www.mdpi.com/2076-2607/11/2/529). Here the true data is in barcodes and 4-6. **This data set is the best choice for someone who wants a large test data set with very deep coverage in an avian host.**

## 2) Install Dependencies and Run PURDY
This section will guied you through how to acquire PURDY,install PURDY's dependencies, and do a basic run with either a test data set or your data set. PURDY is written and bash and does not need to be installed or complied. See the next section to explore available arguments.

### Using Apptainer (most recommended, formerly Singularity)
Without going into details Apptainer is a more secure method of running containers on an HPC system and you can learn more about it here: https://apptainer.org/docs/user/main/index.html
In this case we will be using Apptainer to run a Docker container. Docker is a container system that allows you to run PURDY in an environment we created that already contains all the dependencies you need. For more information about Docker check out their website: https://www.docker.com/
You may need to download Apptainer to use it. You will find installation istructions here: https://github.com/apptainer/apptainer/blob/main/INSTALL.md
If you are working on an HPC cluster you may be able to simply load an Apptainer module.

Once you have either installed or loaded Apptainer, to download the docker image via Apptainer simply run a command. This will download the file, "purdydock_latest.sif", in the directory where this command was run. This file is about 3.2GB. Make sure you have the room on your machine for this file before downloading it. Here is the command:
```
apptainer pull -F docker://darwin1990/purdydock
```

After the image has been installed, create the folder and move your data into it. Here the input folder is named "fastq_pass" to match PURDY's default expectation and should contain all the fastq files you want to be part of this run. 
```
mkdir fastq_pass
mv your_data.fastq fastq_pass
```
Here your_data.fastq could be either one or multiple fastq files, but should be all of the data you want included in this PURDY run.


And then To use PURDY simply run this command:
```
apptainer run purdydock_latest.sif
```

This would run PURDY with all default arguments. A more realistic example is the following:
```
apptainer run purdydock_latest.sif -t 12 -o fullPurdyRunOct19
```

Everything folloving "purdydock_latest.sif" is fed directly to PURDY. In this case "-t 12" tells PURDY to use 12 threads and "-o fullPurdyRunOct19" tells PURDY to put the results in a folder called "fullPurdyRunOct19" which will be created if one does not already exist.

### Using Docker
Docker is a container system wich allows you to run PURDY in an environment we created that already contains all the dependencies you need. For more information about Docker check out their website: https://www.docker.com/
To use tihs method you will first need to download docker to the machine you are using to run PURDY. You will find their download options here: https://docs.docker.com/get-docker

If you are working on an HPC cluster you may be able to simply load a Docker module. On the other hand, some HPC systems believe Docker to be a security risk and therefore allow access to docker images only indirectly via Apptianer (formerly Singularity). If you are working an such an HPC systems try the "Using Aptainer" method of installing dependencies and running PURDY instead of this one.

We have uploaded the docker image to Docker Hub at https://hub.docker.com/repository/docker/darwin1990/purdydock/general. This image will take up about 6GB of data on your machine. Ensure that you have room for it before dowloading it. In order to download it go to the directory where your data is stored, then load the docker image in using the command: 
```
docker pull darwin1990/purdydock
```

Then create the input and output folders. Here the input folder is named "fastq_pass" to match PURDY's default expectation and should contain all the fastq files you want to be part of this run. If you're using Docker directly rather than Apptainer you will have to create a folder for the output even if you are using the default output folder, "fastq_pass_Demultiplexed", for Docker to see your input and write an output to a place where you can access it.
```
mkdir fastq_pass
mv your_data.fastq fastq_pass

mkdir fastq_pass_Demultiplexed
docker run -v "$(pwd)/fastq_pass":"/fastq_pass" -v "$(pwd)/fastq_pass_Demultiplexed":"/fastq_pass_Demultiplexed" darwin1990/purdydock
```

Here your_data.fastq could be either one or multiple fastq files, but should be all of the data you want included in this PURDY run. The `-v` command allows docker access to read and write to the folders "fastq_pass" and "fastq_pass_Demultiplexed". This command runs PURDY with all default arguments. A more realistic example is the following:

```
mkdir fastq_pass
mv your_data.fastq fastq_pass

mkdir fullPurdyRunOct19
docker run -v "$(pwd)/fastq_pass":"/fastq_pass" -v "$(pwd)/testRunOct19":"/testRunOct19" darwin1990/purdydock -t 6 -o testRunOct19
```

In this case "-t 6" tells PURDY to use 6 threads and "-o fullPurdyRunOct19" tells PURDY to put the results in a folder called "fullPurdyRunOct19".

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

You will also need to add each of these dependencies to your PATH. Guidance on adding PURDY to your PATH is provided further down in this section which will give you some information on how to add these dependencies to your PATH. Next you will need to install PURDY. Start by cloning this repository and opening up the permissions using the following commands:

```
git clone https://github.com/flu-crew/PURDY
chmod -R +x PURDY/
```

This downloads PURDY, the reference sequences required for PURDY to properly perform post-assembly analysis, and some other files. You will then want to add PURDY to your PATH so that it can be accessed from any folder on your machine by either using the "export" UNIX tool or by editing your .bash_profile file. Using the "export" tool is easier and less dangerous, but is also only a one time fix. Anytime you restart your command-line interface you will need to do this again before using PURDY. This is how that is done:

```
export PATH=$PATH:path/to/Scripts_folder
```

Where path/to/Scripts_folder is the full path to the folder called "Scripts" that came with this downloaded git repository. If you are in the same folder where you cloned this git repository it will look like this:
```
cd PURDY/Scripts
export PATH=$PATH:"$(pwd)"
```

A better but harder and more dangerous solution is to edit the file in your home folder called .bash_profile which, if it exists, is always in your home directory. DO NOT edit this file in a Graphical User Interphase text editor. The formatting that some of them do automatically can make this file impossible to interpret by your kernal and could potentially damage your ability to use your command-line interface at all. Use only a command-line text editor like Vim, GNU nano, or Emacs. If you are unfamiliar with these editors and aren't confident in your ability to learn them simply use the "export method" rather than risk the functional operation of your command-line interface. If it exists add the following line to it:
```
PATH=$PATH:path/to/Scripts_folder
```

If it does not exist you can create simply create it first with.
```
touch ~/.bash_profile
```

Now, test that PURDY was successfully added to your path by restarting your command-line interface then going to a folder outside of the Scripts folder and typing:
```
purdy -h
```

You should see the help menu which looks something like this:
```
    ##########################################################################
                       Welcome to purdy version 1.0.0!
    ##########################################################################
    Dependencies for this program are guppy, r, and IRMA
    For this help menu use the argument -h

    WARNING: ENSURE THAT YOU ARE NOT RUNNING THIS ON THE HEADNODE!
    WARNING: ENSURE THAT IRMA IS IN YOUR PATH

    Arguments:
        -i : Input directory. Default is 'fastq_pass'
        -o : Output directory. Default is 'fastq_pass_Demultiplexed'
        -t : Number of threads. Default is 1
	-a : Assemly folder for storing the output of IRMA within each barcode
             folder inside of the demultiplexing birectory. Default is 
             "assembly"
        -s : Skip a portion of purdy. Options: '0' = skip nothing, 
             'g' = skip guppy demultiplexing, 'i' = skip IRMA assembly,
             'c' = skip collecting IRMA results into combined fasta files,
             and skip QC statistic calculations, 'm' = skip MAFFT assembly
              and FastTree ML tree construction, and 's' = skip swine clade 
             prediction. These options may be combined. Default is 0.

        --version : prints the version number
```


After dependencies and PURDY are installed and added to your PATH, create the folder and move your data into it. Here the input folder is named "fastq_pass" to match PURDY's default expectation and should contain all the fastq files you want to be part of this run. 
```
mkdir fastq_pass
mv your_data.fastq fastq_pass
```

Here your_data.fastq could be either one or multiple fastq files, but should be all of the data you want included in this PURDY run. After your input folder is prepared PURDY can be run directly using the following basic command:
```
purdy
```

This assumes all default parameters including an input folder called "fastq_pass" and an output folder called "fastq_pass_Demultiplexed" A more realistic example is the following:

```
purdy -t 6 -o testRunOct19
```

In this case "-t 6" tells PURDY to use 6 threads and "-o fullPurdyRunOct19" tells PURDY to put the results in a folder called "fullPurdyRunOct19" which will be created if one does not already exist.



# PURDY's Arguments (user options)

All of PURDY's arguments are laid out in the help menu. This menu can be accessed by typing `purdy -h`, `purdy --help`, or making any mistakes while calling PURDY.  The help menu looks like so:
```
    ##########################################################################
                       Welcome to purdy version 1.0.0!
    ##########################################################################
    Dependencies for this program are guppy, r, and IRMA
    For this help menu use the argument -h

    WARNING: ENSURE THAT YOU ARE NOT RUNNING THIS ON THE HEADNODE!
    WARNING: ENSURE THAT IRMA IS IN YOUR PATH

    Arguments:
        -i : Input directory. Default is 'fastq_pass'
        -o : Output directory. Default is 'fastq_pass_Demultiplexed'
        -t : Number of threads. Default is 1
	-a : Assemly folder for storing the output of IRMA within each barcode
             folder inside of the demultiplexing birectory. Default is 
             "assembly"
        -s : Skip a portion of purdy. Options: '0' = skip nothing, 
             'g' = skip guppy demultiplexing, 'i' = skip IRMA assembly,
             'c' = skip collecting IRMA results into combined fasta files,
             and skip QC statistic calculations, 'm' = skip MAFFT assembly
              and FastTree ML tree construction, and 's' = skip swine clade 
             prediction. These options may be combined. Default is 0.

        --version : prints the version number
```

For the average user the arguments `-i`, `-o`, and `-t` are the only important ones. The arguments `-i` and `-o` allow the user to specify the name of the input and output folders, whereas `-t` allows the user to specify the number of threads to use. The number of threads is used for both demultiplexing using Guppy and alignment of user data with reference sequences using MAFFT. The following example command specifies `-i`, `-o`, and `-t`:

```
purdy -i inputSeqs -o testRunOct19 -t 16
```

If the user wants to rename the folder where IRMA puts the assembled sequences before PURDY works with them they can specify a new name with the argument `-a`. The following example command specifies `-a`:

```
purdy -a IrmasOutput 
```

PURDY can also be operated in a modular fashion using the `-s` argument. This argument allows the user to skip one of PURDY's steps. One use case for this is if someone is simply not interested in one or all of the analysis tools and just wants to do demultiplexing and assembly including PURDY's assistance with data interpretation. The following example command would skip all analysis tools:

```
purdy -s ms
```

Another use case for the `-s` argument is if someone has already run PURDY and it failed in the middle (in the example during IRMA assembly) or if someone has already completed demultiplexing. and wants to start with IRMA assembly. The following example command would accomplish this:

```
purdy -s g
```

For more information on PURDY and all of its arguments see Hufnagel et al. 2023 (XXXXXX)
