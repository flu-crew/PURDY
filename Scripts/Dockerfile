FROM ubuntu:22.04


#Install fortran compiler and some other nice compilers
RUN apt-get update -y && apt-get upgrade -y
RUN apt update -y && apt-get upgrade -y
RUN apt install -y gfortran build-essential


#install most dependencies
RUN apt-get install -y python3.9
RUN apt install -y git mafft python3-pip pigz wget fasttree zlib1g pigz
RUN curl -L http://xrl.us/installperlnix | bash
RUN pip3 install --upgrade pip


#install samtools
RUN apt install -y libncurses-dev libbz2-dev liblzma-dev
RUN wget https://github.com/samtools/samtools/releases/download/1.12/samtools-1.12.tar.bz2 && \
  tar xvjf samtools-1.12.tar.bz2 && \
  cd samtools-1.12/ && \
  ./configure && \
  make && \
  make install && \
  export PATH="$PATH:$(pwd)"  && \
  cd ..


#istall R 4.2.0
RUN cp /etc/apt/sources.list /etc/apt/sources.list~
RUN sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list

RUN apt install -y fort77 xorg-dev liblzma-dev libblas-dev gcc-multilib gobjc++  #for R 3.1 and R 3.2
RUN apt install -y libbz2-dev libpcre2-dev #for R 4.1.2  libpcre2-posix2
RUN apt update -y && apt install -y libpcre3 libpcre3-dev libcurl4-openssl-dev
RUN apt install -y aptitude
RUN aptitude install libreadline-dev

RUN wget https://cran.r-project.org/src/base/R-4/R-4.2.0.tar.gz && \
  tar -xf R-4.2.0.tar.gz && \
  cd R-4.2.0 && \
  ./configure && \
  make -j9 && \
  make install && \
  cd ..


#Copy over custom variant of IRMA
#COPY ./irma_tka ./irma_tka
#RUN chmod -R 777 /irma_tka
#ENV PATH="${PATH}:/irma_tka"

#Install IRMA
RUN wget https://wonder.cdc.gov/amd/flu/irma/flu-amd-202209.zip
RUN unzip flu-amd-202209.zip
RUN sed -i 's/TMP=\/tmp/TMP="$(pwd)"/g' flu-amd/IRMA_RES/modules/FLU/init.sh 
ENV PATH="${PATH}:/flu-amd"

#install classlog
RUN pip3 install click scikit-learn numpy pandas 
RUN pip3 install pybind11
RUN pip3 install setuptools wheel scipy #sklearn 

RUN git clone https://github.com/flu-crew/classLog.git && \
  cd classLog && \
  git clone https://github.com/arendsee/rpalign.git && \
  cd rpalign && \
  pip3 install . && \
  cd .. && \
  pip3 install . && \
  cd ..

#installing PURDY
COPY ./purdy ./purdy
COPY ./REFS ./REFS
ENV PATH="${PATH}:/"

#setting up the file to run upon the call "docker run ..."
ENTRYPOINT ["purdy"]
