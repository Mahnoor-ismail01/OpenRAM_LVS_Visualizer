*INV netlist

.subckt INV A Z vdd gnd
X0 Z A vdd vdd sky130_fd_pr__pfet_01v8 w=0.84u l=0.15u
X1 Z A gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
.ends
