astart=3.00
astep=0.05
n=25

BIN=vasp
echo "lat,ene" > Ni_fcc_energy.csv
for((b=0;b<=$n;b++))
do
i=`echo "$astart+$astep*$b" | bc`
cat > POSCAR << !
# Fcc Ni oriented X=[100] Y=[010] Z=[001].
$i
1.0      0.0        0.0
0.0      1.0        0.0
0.0      0.0        1.0
Ni
4
Direct
0.00000000        0.00000000        0.00000000
0.50000000        0.50000000        0.00000000
0.00000000        0.50000000        0.50000000
0.50000000        0.00000000        0.50000000	
!
$BIN
E=`tail -1 OSZICAR | awk '{print $5}'`
echo "$i,$E" >> Ni_fcc_energy.csv
done
