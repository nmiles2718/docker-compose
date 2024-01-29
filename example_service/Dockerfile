FROM redhat/ubi9:9.3

RUN mkdir /example_service/
RUN yum update -y
ENV PATH=/root/miniconda3/bin:${PATH}
ARG PATH=/root/miniconda3/bin:${PATH}
RUN curl -OL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash ./Miniconda3-latest-Linux-x86_64.sh -b -p /root/miniconda3/
RUN conda init && conda update -y conda
COPY ["py310.yml","example.py", "/example_service/"]
RUN conda env create -f /example_service/py310.yml
RUN echo "conda activate py310" >> ~/.bashrc
ENV PATH=/root/miniconda3/envs/py310/bin:$PATH

