import numpy as np

def sig(x):
    return 1/(1+np.exp(-x))

x=np.array([[0.05,0.10]
])
#print(x)

y=np.array([[0.01,0.99]])
wh=np.array([[.15,.25],
             [0.20,0.30]
    ])
#wh is the weight of hidden layer
#print(wh)

bh=.35

neth=x.dot(wh)+bh

outh=sig(neth)

#printing the net input for first feed forward and output of hiddenlayer
print("Input for hidden Layer forward pass")
print(neth)
print("Output for hidden Layer forward pass")
print(outh)

#now output layer e input jabe outh
#wo is weights for output layer
wo=np.array([[0.40 ,0.50]
            ,[0.45 ,0.55]
             ])
bo=0.60
net_out_o=outh.dot(wo)+bo
#print(net_out_o)

out_o=sig(net_out_o)

#print(out_o)
#error counting using error=(1/2)(target-output)^2
E=((y-out_o)**2)*0.5

#print(E)
totError=np.sum(E,axis=1)

#totError after first iter
#print(totError)


d_total_with_r_to_out_o=-(y-out_o)

#print(d_total_with_r_to_out_o)

d_out_o_with_r_to_net_out_o=out_o*(1-out_o)

#print(d_out_o_with_r_to_net_out_o)

d_net_out_o_with_r_to_wo=outh

#print(d_net_out_o_with_r_to_wo)



#so now we can get d_total_with_r_to_wo

d_total_with_r_to_wo=d_total_with_r_to_out_o.__mul__(d_out_o_with_r_to_net_out_o)
d_total_with_r_to_wo=d_total_with_r_to_wo.__mul__(d_net_out_o_with_r_to_wo)


#print(d_total_with_r_to_wo)

#print(wo)


updated_wo=wo-d_total_with_r_to_wo*0.5
print("Updated weights for output layer:")
print(updated_wo)

print("d_out_o/d_net_o:")
print(d_out_o_with_r_to_net_out_o)

print("e_o/out_o:")
print(d_total_with_r_to_out_o)


print("now we update stuff for hidden layer:")
#d_total/d_wh=(d_total/d_outh)*(d_outh/d_neth)*(d_neth/d_wh)
#d_total/outh=(d_total/d_net_out_O)*(d_net_out_o/d_outh) **
#d_total/d_net_out_o=(d_total/d_out_o)*(d_out_o/d_net_out_o) **

d_total_with_r_to_net_out_o=d_total_with_r_to_out_o*d_out_o_with_r_to_net_out_o
print(d_total_with_r_to_net_out_o)


d_fintotal_with_r_to_outh=(d_total_with_r_to_net_out_o*wo)

#print(d_fintotal_with_r_to_outh)

#y1 = x[:,0]+x[:,2]
d_fintotal_with_r_to_outh=d_fintotal_with_r_to_outh[:,0]+d_fintotal_with_r_to_outh[:,1]
print("d_total/d_outh:")
#d_fintotal_with_r_to_outh=d_fintotal_with_r_to_outh[[0,0]]
#print(d_fintotal_with_r_to_outh)
d_fintotal_with_r_to_outh=d_fintotal_with_r_to_outh[[0,0]]
#print(d_fintotal_with_r_to_outh)
d_total_with_r_to_out_h=d_fintotal_with_r_to_outh[:1]
#print(d_total_with_r_to_out_h)

d_out_h_with_r_to_d_net_h=outh*(1-outh)

#print(d_out_h_with_r_to_d_net_h)

#print(d_total_with_r_to_out_h.dot(d_out_h_with_r_to_d_net_h))
temp=(d_total_with_r_to_out_h.dot(d_out_h_with_r_to_d_net_h))
print(x*temp)
finaltemp=x*temp*0.5
finaltemp=finaltemp.reshape(2,1)
print(wh-finaltemp)




