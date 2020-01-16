function [score1]=CMF(A,lambda1,lambda2,lambdaC,lambdaG)
[m,n]=size(A);
r=fix(n/10);
Y=SM(A');
X=SM(A);
A1=A;
[~,m]=size(X);
[~,n]=size(Y);
rand('state',0) 
H=rand(m,r);
rand('state',2)
W=rand(n,r);
I=eye(r);
k=1;
err = 1e-5;
insweep =2000;
while k<insweep
    k=k+1;
    H=(A*W+lambdaG*X*H)/((W'*W+lambda1*I+lambdaG*H'*H));
    W=(A'*H+lambdaC*Y*W)/(H'*H+lambda2*I+lambdaC*W'*W);
     error = mean(mean(abs(A-H*W')))/mean(mean(A)); 
     if error< err
            break;
        end        
     
end
score=H*W';
score(score<0)=0;
for i=1:m
    for j=1:n
        if A1(i,j)==0
            A1(i,j)=score(i,j);
        end
    end
 end
score1=A1;
end

