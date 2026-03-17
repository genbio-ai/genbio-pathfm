# GenBio-PathFM: A State-of-the-Art Foundation Model for Histopathology

![Histpathology image.](resources/banner.jpg)

GenBio-PathFM is a histopathology foundation model (FM) from [GenBio AI](https://genbio.ai/). 

At the time of release, GenBio-PathFM is the strongest open-weight histopathology FM and the only state-of-the-art histopathology FM trained exclusively on publicly available data.

The model weights are available on [HuggingFace](https://huggingface.co/genbio-ai/genbio-pathfm).

For more details:
* [GenBio AI Blog Post](https://genbio.ai/genbio-pathfm)
* [Paper](https://raw.githubusercontent.com/genbio-ai/genbio-pathfm/main/resources/paper.pdf)

## Abstract

Recent advancements in histopathology foundation models (FMs) have largely been driven by scaling the training data, often utilizing massive proprietary datasets. However, the long-tailed distribution of morphological features in whole-slide images (WSIs) makes simple scaling inefficient, as common morphologies dominate the learning signal. We introduce GenBio-PathFM, a 1.1B-parameter FM that achieves state-of-the-art performance on public benchmarks while using a fraction of the training data required by current leading models. The efficiency of GenBio-PathFM is underpinned by two primary innovations: an automated data curation pipeline that prioritizes morphological diversity and a novel dual-stage learning strategy which we term JEDI (**JE**PA + **DI**NO). Across the THUNDER, HEST, and PathoROB benchmarks, GenBio-PathFM demonstrates state-of-the-art accuracy and robustness. GenBio-PathFM is the strongest open-weight model to date and the only state-of-the-art model trained exclusively on public data.

![Overview of training procedure for GenBio-PathFM.](resources/main_jedi_training.jpg)

## Inference Example

See [inference.py](genbio-pathfm/inference.py) for an example of loading the model and extracting an embedding. 

## License

GenBio-PathFM is available under the [GenBio AI Community License](LICENSE.txt).

## Reference

If you find our work useful, consider citing our paper:

```
@article{kapse2026genbiopathfm,
  title={GenBio-PathFM: A State-of-the-Art Foundation Model for Histopathology},
  author={Kapse, Saarthak and Aygun, Mehmet and Cole, Elijah and Lundberg, Emma and Song, Le and Xing, Eric P.},
  journal={bioRxiv},
  year={2026}
}
```
