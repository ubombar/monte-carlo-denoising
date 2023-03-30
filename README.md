# Monte Carlo Denoising
## Why?
This is a course project of IG3D, Sorbonne Univeristy's DIGIT Master's Program offering. The goal is to use affinity networks to denoise an image. 

## Method
1. I will create multiple scenes consisting of N in range [0, N_max] cubes, cones, and spheres with different materials. 
2. Then a random camera angle will be selected and a half and full render is gathered from blender. 
3. Using the data, a neural network with similar architecture but smaller will be trained.
4. The resulting image will be fed to a superresolution network (new feature!).
5. We will see how the system performs vs the original full renders.

## Drawbacks
* There is very little time and resources to implement and train the network. This smaller patch size will be selected. 
* Original papers uses more complex objects in more complex combinations and materials, for simplicity we will keep this simple.

## Author
Ufuk Bombar ([ubombar](https://github.com/ubombar)): Computer Science Master's student at Sorbonne University.

## References
1. Işık, M., Mullia, K., Fisher, M., Eisenmann, J., & Gharbi, M. (2021). Interactive Monte Carlo denoising using affinity of neural features. ACM Transactions on Graphics (TOG), 40(4), 1-13.