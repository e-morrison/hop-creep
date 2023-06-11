<h1>Background</h1>

This is a project to investigate a potential biochemical solution to hop creep.

Hop creep is thought to be caused by diastatic enzymes originating from hops during dry hopping ([Cottrell, JASBC 2022](https://www.tandfonline.com/doi/full/10.1080/03610470.2022.2084327)).

The two primary diastatic enzymes responsible are alpha- and beta-amylase. One possible solution to hop creep would be the use **a protease that selectively degrades these two enzymes while leaving foam-active proteins intact**. This project investigates if such a proteolytic approach is feasible.  

As the proteome of <em>Humulus lupulus</em> is not well annotated, orthologous proteins from the closely related <em>Cannabis sativa</em> must be used for this analysis. These are [A0A803QK01 (beta-amylase)](https://www.uniprot.org/uniprotkb/A0A803QK01/entry) and [A0A803QQW1 (alpha-amylase)](https://www.uniprot.org/uniprotkb/A0A803QQW1/entry). These two proteins are our intended targets for proteolytic degradation.

The major foam-active proteins are thought to be LTP1, protein Z, and various barley hordeins ([Hao and Li, JASBC 2006](https://www.tandfonline.com/doi/abs/10.1094/ASBCJ-64-0166), [Blasco et al., Int Microbio 2011](https://diposit.ub.edu/dspace/bitstream/2445/55044/1/614976.pdf)). These are annotated as [P07597 (LTP1)](https://www.uniprot.org/uniprotkb/P07597/entry), [P06293 (Protein Z)](https://www.uniprot.org/uniprotkb/P06293/entry), [P06470 (B1-hordein)](https://www.uniprot.org/uniprotkb/P06470/entry), [P06471 (B3-hordein)](https://www.uniprot.org/uniprotkb/P06471/entry), and [P06472 (C-hordein)](https://www.uniprot.org/uniprotkb/P06472/entry). Our ideal protease would not target, or only minimally degrade, these proteins, to ensure that foam formation is not compromised.

<h1>Setup</h1>

First, create the conda environment:

    conda env create -f environment.yaml
    conda activate hop-creep

Download the latest [MySQL MEROPS release](https://ftp.ebi.ac.uk/pub/databases/merops/current_release/meropsweb121.tar.gz) and place in `data/merops/`.

    wget https://ftp.ebi.ac.uk/pub/databases/merops/current_release/meropsweb121.tar.gz
    mv meropsweb121.tar.gz data/merops/
    tar -zxvf data/merops/meropsweb121.tar.gz






