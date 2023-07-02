# Setting the values
N = 50
S = range(1.0, N, step=0.1)  # Range of values for S
o = range(0.1, 0.9, length=100)  # Range of values for o

# Define the likelihood function
L(S, o) = S * log(o) + (N - S) * log(1.0 - o)

# We need to install the Plots package if not installed
using Plots
gr()  # Use the GR backend for plotting

# Plotting the likelihood function
p2 = Plots.heatmap(S, o, (S, o) -> L(S, o), color=:jet, xlabel="S", ylabel="θ", title="Bird's Eye View of Likelihood")

# Compute and plot the likelihood at S = 25
SS = 25
vline!([SS], label=false, color=:black)  # Vertical line at S = 25
P3 = Plots.plot(o, o -> L(SS, o), label=false, xlabel="θ", title="Likelihood at S = $SS")

# Combine the plots
Plots.plot(p2, P3)
savefig("mle-julia.png")  # Save the combined plot as an image
