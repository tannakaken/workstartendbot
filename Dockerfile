FROM lambci/lambda:build-python3.7
ENV AWS_DEFAULT_REGION ap-northease-1

ADD . .

CMD mkdir -p /var/task/build && \
      pip install -r requirements.txt -t /var/task/build && \
      zip -9 build/deploy_package.zip lambda_function.py && \
      cd build && \
      zip -r9 deploy_package.zip *
