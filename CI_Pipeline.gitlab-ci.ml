stages:
  - build
  - test
  - deploy

variables:
  DOCKER_IMAGE: registry.gitlab.com/libertyshield/v4.1

build:
  stage: build
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE

test:
  stage: test
  image: $DOCKER_IMAGE
  script:
    - python -m unittest discover tests/

airgap_deploy:
  stage: deploy
  only:
    - main
  script:
    - scp -o StrictHostKeyChecking=no ./LibertyShield_v4.1.py airgap@target:/opt/liberty/
    - ssh airgap@target "sudo systemctl restart liberty-shield"
