"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Separator } from "@/components/ui/separator";
import { useLogin } from "./useLogin";

type Mode = "login" | "register";

export function LoginForm() {
  const [mode, setMode] = useState<Mode>("login");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const { login, isLoading, error } = useLogin();

  const handleSubmit = async () => {
    if (mode === "login") {
      const success = await login({ email, password });
      if (success) {
        navigate("/");
      }
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 24 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: "easeOut" }}
      className="flex min-h-screen w-full items-center justify-center bg-black p-4"
    >
      <Card className="w-full max-w-sm border-neutral-200 bg-white text-black">
        <CardHeader className="space-y-1">
          <CardTitle className="text-2xl font-semibold tracking-tight">
            {mode === "login" ? "Iniciar sesión" : "Crear cuenta"}
          </CardTitle>
          <CardDescription className="text-neutral-400">
            {mode === "login"
              ? "Ingresá tus datos para continuar"
              : "Completá tus datos para registrarte"}
          </CardDescription>
        </CardHeader>

        <Tabs
          value={mode}
          onValueChange={(value) => setMode(value as Mode)}
          className="w-full"
        >
          <motion.div className="px-6">
            <TabsList className="grid w-full grid-cols-2 bg-neutral-100">
              <TabsTrigger value="login" className="cursor-pointer">
                Ingresar
              </TabsTrigger>
              <TabsTrigger value="register" className="cursor-pointer">
                Registrarme
              </TabsTrigger>
            </TabsList>
          </motion.div>

          {/* TabsContent vacíos: el contenido real animado va abajo con AnimatePresence,
              pero los dejamos para que shadcn maneje la accesibilidad de las tabs */}
          <TabsContent value="login" />
          <TabsContent value="register" />

          <CardContent className="pt-4">
            <AnimatePresence mode="wait">
              <motion.div
                key={mode}
                initial={{ opacity: 0, x: mode === "login" ? -16 : 16 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: mode === "login" ? 16 : -16 }}
                transition={{ duration: 0.25, ease: "easeInOut" }}
                className="space-y-4"
              >
                <motion.div className="space-y-2">
                  <Label htmlFor="email">Correo electrónico</Label>
                  <Input
                    id="email"
                    type="email"
                    placeholder="vos@ejemplo.com"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="border-neutral-300 bg-white text-black"
                  />
                </motion.div>

                <motion.div className="space-y-2">
                  <Label htmlFor="password">Contraseña</Label>
                  <Input
                    id="password"
                    type="password"
                    placeholder="••••••••"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="border-neutral-300 bg-white text-black"
                  />
                </motion.div>

                <AnimatePresence>
                  {mode === "register" && (
                    <motion.div
                      key="confirm"
                      initial={{ opacity: 0, height: 0 }}
                      animate={{ opacity: 1, height: "auto" }}
                      exit={{ opacity: 0, height: 0 }}
                      transition={{ duration: 0.25 }}
                      className="space-y-2 overflow-hidden"
                    >
                      <Label htmlFor="confirmPassword">
                        Repetir contraseña
                      </Label>
                      <Input
                        id="confirmPassword"
                        type="password"
                        placeholder="••••••••"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        className="border-neutral-300 bg-white text-black"
                      />
                    </motion.div>
                  )}
                </AnimatePresence>
              </motion.div>
            </AnimatePresence>

            {error && <p className="text-sm text-red-500">{error}</p>}
          </CardContent>
        </Tabs>

        <CardFooter className="flex flex-col gap-3">
          <motion.div
            className="w-full"
            whileTap={{ scale: 0.96 }}
            whileHover={{ scale: 1.01 }}
            transition={{ type: "spring", stiffness: 400, damping: 17 }}
          >
            <Button
              onClick={handleSubmit}
              disabled={isLoading}
              className="w-full bg-black text-white hover:bg-neutral-800 cursor-pointer"
            >
              {isLoading
                ? "Ingresando"
                : mode === "login"
                  ? "Ingresar"
                  : "Registrarme"}
            </Button>
          </motion.div>

          <Separator className="bg-neutral-200" />

          <motion.p className="text-center text-sm text-neutral-500">
            {mode === "login" ? (
              <>
                ¿No tenés cuenta?{" "}
                <Button
                  variant="link"
                  className="h-auto p-0 text-black underline underline-offset-4 cursor-pointer"
                  onClick={() => setMode("register")}
                >
                  Registrate
                </Button>
              </>
            ) : (
              <>
                ¿Ya tenés cuenta?{" "}
                <Button
                  variant="link"
                  className="h-auto p-0 text-black underline underline-offset-4 cursor-pointer"
                  onClick={() => setMode("login")}
                >
                  Iniciar sesión
                </Button>
              </>
            )}
          </motion.p>
        </CardFooter>
      </Card>
    </motion.div>
  );
}
