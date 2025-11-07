function [C_num,C_distance]=route_hesitation_index_fast(G)

    [n,~]=size(G);
    C_num=zeros(n,n);                         
    C_distance=zeros(n,n);                 
    i=1;
    while sum(sum(~(C_num+eye(n,n))))~=0    
        i;
        G_temp=G^i;                        
        G_temp=G_temp-diag(diag(G_temp));   
        T = ~C_num;
        G_temp=(~C_num).*G_temp;            
        if sum(sum(G_temp))==0
            break
        else
            C_num=C_num+G_temp;             
            G_temp(G_temp~=0)=1;            
            G_temp;
            G_temp*i;
            C_distance=C_distance+G_temp*i; 
            i=i+1;
        end
    end

