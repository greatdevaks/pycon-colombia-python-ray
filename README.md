# pycon-colombia-python-ray
Repository containing talk material and sample code used during PyCon Colombia 2022 talk titled "Architecting and Running Distributed Python Applications with Ray on Kubernetes".

**Author:**</br>
Anmol Krishan Sachdeva</br>
Hybrid Cloud Architect, Google</br>
[LinkedIn@greatdevaks](https://www.linkedin.com/in/greatdevaks) | [Twitter@greatdevaks](https://www.twitter.com/greatdevaks)

**Deck:**</br>
[Architecting and Running Distributed Python Applications with Ray on Kubernetes](./PyConColombia2022-ArchitectingAndRunningDistributedPythonApplicationsWithRayOnKubernetes-AnmolKrishanSachdeva.pdf)

**Sample Implementation Files:**</br>
- [PI Estimation Ray Python Distributed Code](./estimate_pi.py)</br>
- [Kubernetes Job for PI Estimation](./estimate_py_k8s_job.yaml)</br>

**How to run:**</br>
- Have a Kubernetes Cluster created with 2-3 worker nodes of min. capacity 2 cores and 2 GIB each.
- Clone the upstream [Ray GitHub Repository](https://github.com/ray-project/ray)
- Helm install the Ray chart:
```
helm -n ray install pycon-ray-cluster-00 --create-namespace ./ray/deploy/charts/ray
```

**Check the Kubernetes workloads:**</br>
- Check the Ray Operator pod:
```
kubectl get pods
```
- Check Ray Cluster CRD and the pods in `ray` namespace:
```
kubectl get crd rayclusters.cluster.ray.io
kubectl -n ray get rayclusters
```
- Get Ray Cluster Head Node, Worker Nodes, and Service exposing Head Node:
```
kubectl -n ray get pods,services
```
- Get Ray Autoscaler logs:
```
kubectl logs -f $(kubectl get pods -l cluster.ray.io/component=operator -o custom-columns=:metadata.name)
```
- Get access to Ray Dashboard by port forwarding the Head Service:
```
kubectl -n ray port-forward service/pycon-ray-cluster-00-ray-head 8265:8265
```
**Note:** Open localhost:8265 to open the Ray Dashboard

**Run PI Estimation Kubernetes Job:**</br>
```
# Run a sample Ray program using Kubernetes Job
kubectl -n ray create -f https://raw.githubusercontent.com/greatdevaks/pycon-colombia-python-ray/main/estimate_py_k8s_job.yaml

# View localhost:8265 Ray Dashboard
```

**Cleanup:**</br>
```
# Delete RayCluster Custom Resource
kubectl -n ray delete raycluster pycon-ray-cluster-00

# Delete the Ray Helm Release - doesn't delete the RayCluster CRD
helm -n ray uninstall pycon-ray-cluster-00

# Delete the Ray Kubernetes Namespace
kubectl delete namespace ray

# Delete teh RayCluster CRD
kubectl delete crd rayclusters.cluster.ray.io
```


**References:**
- [Writing Your First Distributed Python Application with Ray](https://www.anyscale.com/blog/writing-your-first-distributed-python-application-with-ray)
- [Scaling Applications with Kubernetes on Ray by Vishnu Deva](https://vishnudeva.medium.com/scaling-applications-on-kubernetes-with-ray-23692eb2e6f0)
- [Official Ray Anyscale Docs](https://docs.anyscale.com/)
- [Autoscaling Clusters with Ray](https://www.anyscale.com/blog/autoscaling-clusters-with-ray)


**Disclaimer:**</br>
The content and the views presented during the talk/session are the author’s own and not of the organizations/companies they are associated with.
