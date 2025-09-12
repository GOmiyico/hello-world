""""绘制带电圆环的电场线及等势面"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.cm as cm
import matplotlib.colors as colors
r0=0.5
Ntht=100
dthe=2*np.pi/Ntht
Ny, Nz,Nx= 5, 5,5
Yl, Zb, Yr, Zt,Xl,Xr= -1, -1, 1, 1,-1,1
#dy,dz,dx= (Yr-Yl)/Ny, (Zt-Zb)/Nz,(Xr-Xl)/Ny
dy,dz,dx= (Yr-Yl)/Ny, (Zt-Zb)/Nz,(Xr-Xl)/Nx
the=np.linspace(0, 2*np.pi, Ntht+1)
y= np.linspace(Yl, Yr, Ny+1)
z= np.linspace(Zb, Zt, Nz+1)
x=np.linspace(Xl, Xr, Nx+1)
Y,Z,X,T=np.meshgrid(y,z,x,the)
r=np.sqrt((X-r0*np.cos(T))**2+(Y-r0*np.sin(T))**2+Z**2)
r3=r**3+1e-10
#dEy =r0*(Y-r0*np.sin(T))/r3
dEy =r0*Z*np.sin(T)/r3
Ey=dthe*np.trapz(dEy,axis=3)
#dEz =r0*Z/r3
dEz =r0*(r0-Y*np.sin(T)-X*np.cos(T))/r3
Ez=dthe*np.trapz(dEz,axis=3)
#dEx =r0*(X-r0*np.cos(T))/r3
dEx =r0*(Z*np.cos(T))/r3
Ex=dthe*np.trapz(dEx,axis=3)
fig = plt.figure(figsize=(10,5))
ax1=fig.add_subplot(121,projection='3d')

# 创建密度值数组
density = np.sqrt(Ex**2+Ey**2+Ez**2)

# 创建颜色映射
norm = colors.Normalize(vmin=min(density[0,0,:]), vmax=max(density[0,0,:]))
cmap = cm.jet
# 将密度值映射到颜色
arrow_colors = cmap(norm(density[0,0,:]))
ax1.quiver(X[...,0],Y[...,0],Z[...,0],Ex,Ey,Ez,length=0.3,normalize=True,linewidth=0.5) 
plt.title('3d view of E field of charged ring ')
theta = np.linspace(0, 2*np.pi, 100)
x_ring = r0 * np.cos(theta)
z_ring = 0.0
y_ring = r0 * np.sin(theta)
z_ring_array = np.full_like(theta, z_ring)

ax1.plot(x_ring, y_ring, z_ring_array, color='yellow', linewidth=2)
# 显示颜色条
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
plt.colorbar(sm,ax=ax1)
ax2=fig.add_subplot(122)
ax2.axis([-2,2,-2,2])
ax2.set_title('YZ view of E field of charged ring ')
yy,zz=np.meshgrid(y,z)
ax2.set_xlabel('y')
ax2.set_ylabel('z')
ax2.streamplot(yy,zz,Ey[:,:,0],Ez[:,:,0],cmap='autumn',density=0.5)
plt.show()
