import "./three.js";
import { OrbitControls } from "./OrbitControls.js";

let camera, scene, renderer;
let geometry, material, mesh, controls, data;

export function mazePreviewFromFile(file, wireframe) {
  var points = [];
  const reader = new FileReader();
  reader.addEventListener("load", (event) => {
    var text = event.target.result;
    var lines = text.split("\n");

    for (var i in lines) {
      var line = lines[i].split(";");
      for (var j in line) {
        points.push([line[j], j, i]);
      }
    }
    const model = generateModel(points, wireframe);
    mesh.clear();
    mesh.add(model);
  });
  reader.readAsText(file);
}

export async function mazePreviewFromURL(url, wireframe) {
  var points = [];
  var text = "";
  await fetch(url)
    .then((r) => r.text())
    .then((t) => (text = t));
  var lines = text.split("\n");

  for (var i in lines) {
    var line = lines[i].split(";");
    for (var j in line) {
      points.push([line[j], j, i]);
    }
  }
  const model = generateModel(points, wireframe);
  mesh.clear();
  mesh.add(model);
}

function generateModel(points, wireframe) {
  const material = new THREE.MeshStandardMaterial({
    color: 0x008cff,
    wireframe: wireframe,
  });
  const model = new THREE.Group();
  for (var i in points) {
    if (parseInt(points[i][0]) == -1) {
      const geo = new THREE.BoxGeometry(0.1, 0.2, 0.1);
      const pillar = new THREE.Mesh(geo, material);
      pillar.castShadow = true;
      pillar.position.set(
        parseInt(points[i][1]) * 0.1,
        0,
        parseInt(points[i][2]) * 0.1
      );
      model.add(pillar);
    }
  }
  return model;
}

export function render(doc) {
  camera = new THREE.PerspectiveCamera(70, 1, 0.1, 100);
  camera.position.x = 5;
  camera.position.y = 5;
  camera.position.z = 5;
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0xffffff);

  mesh = new THREE.Mesh(
    new THREE.BoxGeometry(0, 0, 0),
    new THREE.MeshStandardMaterial()
  );

  scene.add(mesh);

  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(300, 300);

  renderer.setAnimationLoop(animation);

  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap; // default THREE.PCFShadowMap

  //Create a PointLight and turn on shadows for the light
  const light = new THREE.PointLight(0xffffff, 1, 100);

  light.position.set(10, 10, 10);
  light.castShadow = true; // default false
  scene.add(light);

  //controls = new DragControls( mesh.children, camera, renderer.domElement );
  controls = new OrbitControls(camera, renderer.domElement);
  renderer.render(scene, camera);

  doc.getElementById("preview").appendChild(renderer.domElement);
}

function animation(time) {
  //mesh.rotation.x = time / 2000;
  //mesh.rotation.y = time / 1000;
  renderer.render(scene, camera);
}
