# FluPore: a pipeline for demultiplexing, assembly, and classification of influenza A viruses
Welcome to the GitHub repository and manual for the software FluPore! FluPore is a fast and easy-to-use bash pipeline for Oxford Nanopore Technologies (ONT) influenza A sequences from any host and all gene segments that uses existing tools to perform demultiplexing and assembly, collect and calculate basic assembly statistics, generate phylogenetic trees alongside reference sequences, and classify swine HA sequences. 

A manuscript describing the software is in preparation.

# How to Run FluPore
FluPore is a bash script that has dependencies. For your convenience we have built a docker image which provides an isolated filesystem containing all required dependencies. We recommend that you take advantage of this by either using Docker directly or using Docker indirectly via Apptainer (most recommended; formerly Singularity).

## 1) Download the Test Data Set
We used three reference data sets to demonstrate the capabilities of FluPore. We recommend using the swine host data set as a first run of FluPore to ensure that it is properly working. Note that multiple runs of FluPore on the same data will not yield identical results, but should yield very similar results where real data is involved, as opposed to "junk" where sequencing failed for any reason. The best way to check if your run was successful is to check the output to see if FluPore claims each segment ran successfully (it will tell you directly if something failed) and to compare your phylogenetic tree to the one in the "Test Results" section of this repository. Avian and Human data are also provided in the "Test Results" folder in support of the FluPore manuscript. If you wish, you can skip this step and jump to step 2, "Install Dependencies and Run FluPore" and run FluPore first on your data.

This influenza A H1N1, H1N2, and H3N2 data set was collected from swine hosts in Rambo-Martin et al. 2020 (https://journals.asm.org/doi/full/10.1128/msphere.00822-19). This data has been demultiplexed and basecalled and can be found on NCBI under BioProject PRJNA528211 (https://www.ncbi.nlm.nih.gov/sra?linkname=bioproject_sra_all&from_uid=528211). Search for the Bioproject then look for the link to the 13 SRA experiments if the provided link doesn't work. Here the true data is in barcodes 1,5,6,and 14-23. 

## 2) Install Dependencies and Run FluPore
This section will guide you through how to acquire FluPore, install FluPore's dependencies, and do a basic run with either a test data set or your data set. FluPore is written in bash and does not need to be installed or complied. See the next section to explore available arguments.

### Using Apptainer (recommended)
Without going into details Apptainer is a more secure method of running containers on an HPC system and you can learn more about it here: https://apptainer.org/docs/user/main/index.html
In this case we will be using Apptainer to run a Docker container. Docker is a container system that allows you to run FluPore in an environment we created that already contains all the dependencies you need. For more information about Docker check out their website: https://www.docker.com/
You may need to download Apptainer to use it. You will find installation istructions here: https://github.com/apptainer/apptainer/blob/main/INSTALL.md
If you are working on an HPC cluster you may be able to simply load an Apptainer module.

Once you have either installed or loaded Apptainer, to download the docker image via Apptainer simply run a command. This will download the file, "flupore_latest.sif", in the directory where this command was run. This file is about 3.2GB. Make sure you have the room on your machine for this file before downloading it. Here is the command:
```
apptainer pull -F docker://darwin1990/flupore
```

After the image has been installed, create the folder and move your data into it. Here the input folder is named "fastq_pass" to match FluPore's default expectation and should contain all the fastq files you want to be part of this run. 
```
mkdir fastq_pass
mv your_data.fastq fastq_pass
```
Here your_data.fastq could be either one or multiple fastq files, but should be all of the data you want included in this FluPore run.


And then To use FluPore simply run this command:
```
apptainer run flupore_latest.sif
```

This would run FluPore with all default arguments. A more realistic example is the following:
```
apptainer run flupore_latest.sif -t 12 -o fullFluPoreRunOct19
```

Everything following "flupore_latest.sif" is fed directly to FluPore. In this case "-t 12" tells FluPore to use 12 threads and "-o fullFluPoreRunOct19" tells FluPore to put the results in a folder called "fullFluPoreRunOct19" which will be created if one does not already exist.

### Using Docker
Docker is a container system wich allows you to run FluPore in an environment we created that already contains all the dependencies you need. For more information about Docker check out their website: https://www.docker.com/
To use this method you will first need to download docker to the machine you are using to run FluPore. You will find their download options here: https://docs.docker.com/get-docker

If you are working on an HPC cluster you may be able to simply load a Docker module. On the other hand, some HPC systems believe Docker to be a security risk and therefore allow access to docker images only indirectly via Apptianer (formerly Singularity). If you are working an such an HPC systems try the "Using Aptainer" method of installing dependencies and running FluPore instead of this one.

We have uploaded the docker image to Docker Hub at https://hub.docker.com/repository/docker/darwin1990/flupore/general. This image will take up about 6GB of data on your machine. Ensure that you have room for it before dowloading it. In order to download it go to the directory where your data is stored, then load the docker image in using the command: 
```
docker pull darwin1990/flupore
```

Then create the input and output folders. Here the input folder is named "fastq_pass" to match FluPore's default expectation and should contain all the fastq files you want to be part of this run. If you're using Docker directly rather than Apptainer you will have to create a folder for the output even if you are using the default output folder, "fastq_pass_Demultiplexed", for Docker to see your input and write an output to a place where you can access it.
```
mkdir fastq_pass
mv your_data.fastq fastq_pass

mkdir fastq_pass_Demultiplexed
docker run -v "$(pwd)/fastq_pass":"/fastq_pass" -v "$(pwd)/fastq_pass_Demultiplexed":"/fastq_pass_Demultiplexed" darwin1990/flupore
```

Here your_data.fastq could be either one or multiple fastq files, but should be all of the data you want included in this FluPore run. The `-v` command allows docker access to read and write to the folders "fastq_pass" and "fastq_pass_Demultiplexed". This command runs FluPore with all default arguments. A more realistic example is the following:

```
mkdir fastq_pass
mv your_data.fastq fastq_pass

mkdir fullFluPoreRunOct19
docker run -v "$(pwd)/fastq_pass":"/fastq_pass" -v "$(pwd)/testRunOct19":"/testRunOct19" darwin1990/flupore -t 6 -o testRunOct19
```

In this case "-t 6" tells FluPore to use 6 threads and "-o fullFluPoreRunOct19" tells FluPore to put the results in a folder called "fullFluPoreRunOct19".

### Installing all Dependencies individually (not recommended)
While it is possible to install all of FluPore's dependencies without the docker image it is not recommended. The total number of dependencies is unfortunately quite extensive and there are sometimes conflicts between versions of software which can be hard to predict.  If you choose to take this route despite this warning here are the dependencies you will need to install (some of which have their own dependencies):

Guppy - https://help.nanoporetech.com/en/collections/3738249-guppy

IRMA (using the flu module) - https://wonder.cdc.gov/amd/flu/irma/

R - https://www.r-project.org/

perl - https://www.perl.org/get.html

samtools - http://www.htslib.org/

MAFFT - https://mafft.cbrc.jp/alignment/software/

FastTree - http://www.microbesonline.org/fasttree/

Python3 - https://www.python.org/downloads/

You will also need to add each of these dependencies to your PATH. Guidance on adding FluPore to your PATH is provided further down in this section which will give you some information on how to add these dependencies to your PATH. Next you will need to install FluPore. Start by cloning this repository and opening up the permissions using the following commands:

```
git clone https://github.com/flu-crew/FluPore
chmod -R +x FluPore/Scripts
```

This downloads FluPore, the reference sequences required for FluPore to properly perform post-assembly analysis, and some other files. You will then want to add FluPore to your PATH so that it can be accessed from any folder on your machine by either using the "export" UNIX tool or by editing your .bash_profile file. Using the "export" tool is easier and less dangerous, but is also only a one time fix. Anytime you restart your command-line interface you will need to do this again before using FluPore. This is how that is done:

```
export PATH=$PATH:path/to/Scripts_folder
```

Where path/to/Scripts_folder is the full path to the folder called "Scripts" that came with this downloaded git repository. If you are in the same folder where you cloned this git repository it will look like this:
```
cd FluPore/Scripts
export PATH=$PATH:"$(pwd)"
```

A better but harder solution is to edit the file in your home folder called .bash_profile which, if it exists, is always in your home directory. Use a command-line text editor like Vim, GNU nano, or Emacs. If you are unfamiliar with these editors and aren't confident in your ability to learn them simply use the "export method" rather than risk the functional operation of your command-line interface. If it exists add the following line to it:
```
PATH=$PATH:path/to/Scripts_folder
```

If it does not exist you can create simply create it first with.
```
touch ~/.bash_profile
```

Now, test that FluPore was successfully added to your path by restarting your command-line interface then going to a folder outside of the Scripts folder and typing:
```
flupore -h
```

You should see the help menu which looks something like this:
```
    ##########################################################################
                       Welcome to FluPore version 1.0.0!
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
        -s : Skip a portion of FluPore. Options: '0' = skip nothing, 
             'g' = skip guppy demultiplexing, 'i' = skip IRMA assembly,
             'c' = skip collecting IRMA results into combined fasta files,
             and skip QC statistic calculations, 'm' = skip MAFFT assembly
              and FastTree ML tree construction, and 's' = skip swine clade 
             prediction. These options may be combined. Default is 0.

        --version : prints the version number
```


After dependencies and FluPore are installed and added to your PATH, create the folder and move your data into it. Here the input folder is named "fastq_pass" to match FluPore's default expectation and should contain all the fastq files you want to be part of this run. 
```
mkdir fastq_pass
mv your_data.fastq fastq_pass
```

Here your_data.fastq could be either one or multiple fastq files, but should be all of the data you want included in this FluPore run. After your input folder is prepared FluPore can be run directly using the following basic command:
```
flupore
```

This assumes all default parameters including an input folder called "fastq_pass" and an output folder called "fastq_pass_Demultiplexed" A more realistic example is the following:

```
flupore -t 6 -o testRunOct19
```

In this case "-t 6" tells FluPore to use 6 threads and "-o fullFluPoreRunOct19" tells FluPore to put the results in a folder called "fullFluPoreRunOct19" which will be created if one does not already exist.



# FluPore's Arguments (user options)

All of FluPore's arguments are laid out in the help menu. This menu can be accessed by typing `flupore -h`, `flupore --help`, or making any mistakes while calling FluPore.  The help menu looks like so:
```
    ##########################################################################
                       Welcome to FluPore version 1.0.0!
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
        -s : Skip a portion of FluPore. Options: '0' = skip nothing, 
             'g' = skip guppy demultiplexing, 'i' = skip IRMA assembly,
             'c' = skip collecting IRMA results into combined fasta files,
             and skip QC statistic calculations, 'm' = skip MAFFT assembly
              and FastTree ML tree construction, and 's' = skip swine clade 
             prediction. These options may be combined. Default is 0.

        --version : prints the version number
```

For many users the arguments `-i`, `-o`, and `-t` are the only important ones. The arguments `-i` and `-o` allow the user to specify the name of the input and output folders, whereas `-t` allows the user to specify the number of threads to use. The number of threads is used for both demultiplexing using Guppy and alignment of user data with reference sequences using MAFFT. The following example command specifies `-i`, `-o`, and `-t`:

```
flupore -i inputSeqs -o testRunOct19 -t 16
```

If the user wants to rename the folder where IRMA puts the assembled sequences before FluPore works with them they can specify a new name with the argument `-a`. The following example command specifies `-a`:

```
flupore -a IrmasOutput 
```

FluPore can also be operated in a modular fashion using the `-s` argument. This argument allows the user to skip one or more of FluPore's steps. One use case for this is if someone is simply not interested in one or all of the analysis tools and just wants to do demultiplexing and assembly including FluPore's assistance with data interpretation. The following example command would skip all analysis tools:

```
flupore -s ms
```

Another use case for the `-s` argument is if someone has already run FluPore and it failed in the middle (in the example during IRMA assembly) or if someone has already completed demultiplexing and wants to start with IRMA assembly. The following example command would accomplish this:

```
flupore -s g
```

For more information on FluPore and all of its arguments see Hufnagel et al. 2023 (XXXXXX)
