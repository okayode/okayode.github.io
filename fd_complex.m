% Complex step example.  Requires Symbolic Math Toolbox.
% see Dr. Nick Higham's what is note https://nhigham.com/2020/10/06/what-is-the-complex-step-approximation/

clear;
clc;
format long

b = exp(1); %b = 2, 3, exp(1)
syms x; f = b^x;

% Derivative at $a = 0$:
a = 0; 
%fd = double(subs( diff(f), a));

% Convert symbolic function to MATLAB function.
f = matlabFunction(f);  

% Finite difference approximations with step $h$:
h = [1, 0.5, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001];
for j = 1:length(h)
    i = sqrt(-1);
    fd = (f(a+h(j))-f(a))/h(j);             % derivative approach discussed in class
    fc = imag( f(a + i*h(j)))/h(j);  % Complex approximation 
    fprintf('\n h = %f, (%i^h - 1)/h = %f , %i^(sqrt(-1)h)/h = %f\n',h(j), b, fd, b, fc);
end

