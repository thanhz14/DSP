### transverse self-polarization or diamagnetic term. $ ^{[24]} $

The molecular Hamiltonian describes the vibrational modes as harmonic oscillators which are coupled to each other by a third order anharmonic coupling term. This term is obtained by using a Taylor expansion of the harmonic potential and therefore includes a mediator for the IVR pathways in the model. So the molecular Hamiltonian for two separate modes (q, Q) in the molecular part is described by:

 $$ \hat{H}_{m o l}=\hbar\omega_{q}(\hat{b}^{\dagger}\hat{b})+\hbar\omega_{Q}(\hat{c}^{\dagger}\hat{c})+\sum_{\tau,s}^{3}\eta_{\tau,s}^{e Q}\left(\hat{b}^{\dagger}+\hat{b}\right)^{\tau}\left(\hat{c}^{\dagger}+\hat{c}\right)^{\tau}. $$ 

Here  $ \omega_{i} $ describes the fundamental frequency of the molecular mode  $ q $ which is coupled to the cavity and the respective degrees of freedom are expressed with the ladder operators,  $ \psi $ and  $ \hat{b} $. In the second part, a lower energy vibrational mode  $ Q $ is described with its respective frequency  $ \omega_{Q} $ and the corresponding ladder operators ( $ \hat{c}^{i} $,  $ \hat{c} $). The last term describes the general form of the third order couplings, where  $ n_{k,i} $ describes the anharmonic coupling constants and will be referred to by  $ \hat{W}^{i,j} $. To obtain the corresponding eigenvector for the upper and lower polariton, the Hamiltonian matrix is diagonalized. By doing this one arrives at the following expression for the polaritons:

 $$ |\psi_{(U P,L P)};0\rangle=\frac{|1_{c},0,0\rangle\pm|0_{c},1,0\rangle}{\sqrt{2}}. $$ 

Here the uncoupled states are described by the kets where the first term describes the excitation in the cavity state, the second term describes the excitation in the high frequency mode and the last term is the excitation in the Q mode.

Under specific symmetry considerations not all intramolecular coupling orders  $ (r, s) $ are relevant. In this specific case only orders with  $ r + s \leq 3 $ are considered. Since all considered coordinates are intramolecular normal modes the bilinear coupling  $ (1, 1) $ is in this case equal to zero. Generally, all terms of the potential energy have to transform according to the totally symmetric representation of the molecules point group. $ ^{[25]} $ Thus according to the following equation:

#### 2.1.2 Anharmonic Coupling Terms

 $$ \left(\Gamma^{(i)}\right)^{r}\times\left(\Gamma^{(Q)}\right)^{s}\subset\Gamma_{A}. $$ 

Since the models discussed in this work modeled after the octahedral W(CO) $ _{6} $ molecule and thus exhibit non-Abelian point group symmetry, the various possible couplings have

 $$ \Psi\left(q_{1},...,q_{f},t\right)=\sum_{j_{1}=1}^{N_{1}}...\sum_{j_{f}=1}^{N_{f}}C_{j_{1}...j_{f}}(t)\prod_{s=1}^{f}\chi_{j_{k}}^{s}\left(q_{s}\right) $$ 

time-independent basis-set functions.

Hereby, f represents the degrees of freedom (DOF),  $ C_{j_1 \ldots j_t}(t) $ denotes the time-dependent expansion coefficients and  $ N_\kappa $ describes the number of basis functions used for representing the  $ \kappa $th DOF. The orthogonal time-independent primitive basis functions are represented by  $ \chi_{\kappa}^\kappa(g_\kappa) $ and only the time-dependent expansion coefficients are optimized variationally. $ ^{[81,82]} $

The problem with the standard method is the exponential scaling as the number of coefficients increases with  $ N^{f} $. Therefore, the standard method is only suited for problems with less than 6 DOFs.

In the multiconfiguration time-dependent Hartree method (MCTDH method) the scaling is softened by introducing a smaller but now time-dependent basis, the so-called single particle functions (SPFs)

 $$ \left|\varphi_{j_{k}}^{n}\left(q_{k},t\right)\right\rangle=\sum_{i_{n}=1}^{N_{n}}c_{i_{n},j_{n}}^{(s)}\left(t\right)\left|\chi_{i_{n}}^{(s)}\left(q_{n}\right)\right\rangle $$ 

The SPFs are represented as a linear combination of the time-independent primitive basis functions. The ansatz for MCTDH method can now be written as the following:

 $$ \begin{align*}\Psi\left(q_{1},\ldots,q_{f},t\right)&=\sum_{j_{1}=1}^{n_{1}}-\sum_{j_{f}=1}^{n_{f}}A_{j_{1}\ldots j_{f}}(t)\prod_{n=1}^{f}\varphi_{jk}^{n}\left(q_{n},t\right)\\&=\sum_{J}A_{J}\Phi_{J}.\end{align*} $$ 

Where  $ \Phi_{J} $ describes the f-dimensional product of the SPFs, the Hartree product. The complex expansion coefficients  $ A_{J} $ and the basis functions  $ \varphi_{jk}^{s}(q_{k},t) $ are both time-dependent and optimized variations. [31,32]

Due to the fact that a two layer scheme was used here (the time-dependent SPFs and the primitive basis), the exponential scaling of the DOFs, as  $ n_{k} $, is smaller compared to the layer method like the standard method.

By now applying the Dirac-Frenchle variational principle to the ansatz (eq. (2.9)), we obtain the respective Equations of Motion and therefore a set of coupled differential

#### 2.1. Molecules in Cavities

The molecular Hamiltonian describes the vibrational modes as harmonic oscillators which are coupled to each other by a third order anharmonic coupling term. This term is obtained by using a Taylor expansion of the harmonic potential and therefore includes a mediator for the IVR pathways in the model. So the molecular Hamiltonian for two separate modes (q, Q) in the molecular part is described by:

 $$ \dot{H}_{m o d}=\hbar\omega_{q}(\dot{\hat{b}}^{\dagger}\dot{\hat{b}})+\hbar\omega_{Q}(\dot{c}^{\dagger}\dot{c})+\sum_{n,s}^{s}x_{n,s}^{q Q}\left(\dot{\hat{b}}^{\dagger}+\dot{\hat{b}}\right)^{s}\left(\dot{c}^{\dagger}+\dot{c}\right)^{s}. $$ 

Here  $ \omega_{q} $ describes the fundamental frequency of the molecular mode q which is coupled to the cavity and the respective degrees of freedom are expressed with the ladder operators,  $ \hat{b}^{j} $ and  $ \hat{b}_{k} $. In the second part, a lower energy vibrational mode Q is described with its respective frequency  $ \omega_{Q} $ and the corresponding ladder operators  $ (\hat{c}^{j}, \hat{c}) $. The last term describes the general form of the third order couplings, where  $ \eta_{q} $ describes the anharmonic coupling constants and will be referred to by  $ \hat{W}^{j}[q] $. To obtain the corresponding eigenvector for the upper and lower polariton, the Hamiltonian matrix is diagonalized. By doing this one arrives at the following expression for the polariton: [22, 25]

 $$ [\psi_{(U P,L P)};0)=\frac{|1_{v},0,0)\pm|0_{v},1,0\rangle}{\sqrt{2}}. $$ 

Here the uncospled states are described by the kots where the first term describes the excitation in the cavity state, the second term describes the excitation in the high frequency mode and the last term is the excitation in the Q mode.

##### 2.1.2. Anharmonic Coupling Terms

Under specific symmetry considerations not all intramolecular coupling orders  $ (r, s) $ are relevant. In this specific case only orders with  $ r + s \leq 3 $ are considered. Since all considered coordinates are intramolecular normal modes the bilinear coupling  $ (1, 1) $ is in this case equal to zero. Generally, all terms of the potential energy have to transform according to the totally symmetric representation of the molecules point group. $ ^{[26]} $ Thus according to the following equation:

Since the models discussed in this work modeled after the octahedral W(CO) $ _{6} $ molecule and thus exhibit non-Abelian point group symmetry, the various possible couplings have

 $$ \left(\Gamma^{(q)}\right)^{r}\times\left(\Gamma^{(Q)}\right)^{s}\subset\Gamma_{A}. $$ 

time-independent basis-set functions.

 $$ \Phi\left(\boldsymbol{q}_{1},--,\boldsymbol{q}_{f},t\right)=\sum_{j_{k}=1}^{N_{i}}-\sum_{j_{f}=1}^{N_{f}}C_{j_{k},-j_{f}}\left(t\right)\prod_{n=1}^{f}\chi_{j_{k}}^{n}\left(\boldsymbol{q}_{k}\right) $$ 

Hereby, $f$ represents the degree of freedom (DOF), $C_{2i-j_f}(t)$ denotes the time-dependent expansion coefficients and $N_s$ describes the number of basis functions used for representing the $t$th DOF. The orthonormal time-independent primitive basis functions are represented by $\chi_{2i}^n(q_n)$ and only the time-dependent expansion coefficients are optimized variationally [31, 32].

The problem with the standard method is the exponential scaling as the number of coefficients increases with  $ N' $. Therefore, the standard method is only suited for problems with less than 6 DOFs.

In the multiconfiguration time-dependent Hartree method (MCTDH method) the scaling is softened by introducing a smaller but now time-dependent basis, the so-called single particle functions (SPFs)

 $$ \left|\varphi_{2k}^{n}\left(\mathfrak{g}_{k},t\right)\right\rangle=\sum_{i_{k}=1}^{N_{n}}c_{i_{k},j_{k}}^{(n)}\left(t\right)\left|\chi_{i_{k}}^{(n)}\left(\mathfrak{g}_{k}\right)\right\rangle. $$ 

The SPFs are represented as a linear combination of the time-independent primitive basis functions. The anats for MCTDH method can now be written as the following:

 $$ \begin{align*}\Psi\left(q_{1},...,q_{f},t\right)=\sum_{j=1}^{n_{1}}-\sum_{j f=1}^{n f}A_{j1...j f}(t)\prod_{n=1}^{f}\varphi_{2h}^{n}\left(q_{k},t\right)\\=\sum A_{j}\Phi,\end{align*} $$ 

Where  $ \Phi_{j} $ describes the f-dimensional product of the SPFs, the Hartree product. The complex expansion coefficients  $ A_{j} $ and the basis functions  $ \varphi_{j_{k}}^{n}(q_{k},t) $ are both time-dependent and optimized variationsally [31, 32].

Due to the fact that a two layer scheme was used here (the time-dependent SPFs and the primitive basis), the exponential scaling of the DOFs, as  $ n_{k} $, is smaller compared to the one layer method like the standard method.

By now applying the Direct-Frenchle variational principle to the asmatz (eq. (2.9)), we obtain the respective Equations of Motion and therefore a set of coupled differential

<div style="text-align: center;">Figure B.3: Scan of a modern thesis with a mobile device camera, with permission from the author.</div>
